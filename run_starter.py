from helper import *
import mysql.connector
import random
import os

logger = logging.getLogger()

def main():
    config = yaml.load(open("config_starter.yaml", "r"), Loader=yaml.FullLoader)
    os.environ["OPENAI_API_KEY"] = config["openai_api_key"]

    logging.basicConfig(
        format="%(message)s",
        handlers=[logging.StreamHandler(ColorPrint())],
    )
    logger.setLevel(logging.INFO)

    scenario = input(
        "Please select a scenario (trello/tmdb): "
    )

    scenario = scenario.lower()
    api_spec, headers = None, None

    if scenario == "tmdb":
        os.environ["TMDB_ACCESS_TOKEN"] = config["tmdb_access_token"]
        api_spec, headers = process_spec_file(
            file_path="specs/tmdb_oas.json", token=os.environ["TMDB_ACCESS_TOKEN"]
        )
        query_example = "Give me the number of movies directed by Sofia Coppola"

    elif scenario == "trello":
        key = config["trello_api_key"]
        token = config["trello_token"]
        
        os.environ["TRELLO_API_KEY"] = key
        os.environ["TRELLO_TOKEN"] = token
            
        replace_api_credentials_in_json(
            ###to replace all the key and token variables in the specs file with real values
            scenario=scenario,
            actual_key=key,
            actual_token=token
        )
        api_spec, headers = process_spec_file(  ### to make the specs file minfy or smaller for for better processing
            file_path="specs/trello_oas.json",
            token=os.environ["TRELLO_TOKEN"],
            key=os.environ["TRELLO_API_KEY"]
        )

        replace_api_credentials(
            model="api_selector",
            scenario=scenario,
            actual_key=os.environ["TRELLO_API_KEY"],
            actual_token=os.environ["TRELLO_TOKEN"]
        )
        replace_api_credentials(
            model="planner",
            scenario=scenario,
            actual_key=os.environ["TRELLO_API_KEY"],
            actual_token=os.environ["TRELLO_TOKEN"]
        )

        query_example = "Create a new board with name 'abc_board'"

    else:
        raise ValueError(f"Unsupported scenario: {scenario}")

    populate_api_selector_icl_examples(scenario=scenario)
    populate_planner_icl_examples(scenario=scenario)

    requests_wrapper = Requests(headers=headers)

    # text-davinci-003
    llm = OpenAI(model_name="gpt-4-turbo", temperature=0.0, max_tokens=2048)
    api_llm = ApiLLM(
        llm,
        api_spec=api_spec,
        scenario=scenario,
        requests_wrapper=requests_wrapper,
        simple_parser=False,
    )

    print(f"Example instruction: {query_example}")
    query = input(
        "Please input an instruction (Press ENTER to use the example instruction): "
    )
    if query == "":
        query = query_example

    logger.info(f"Query: {query}")

    start_time = time.time()
    api_llm.run(query)
    logger.info(f"Execution Time: {time.time() - start_time}")

if __name__ == "__main__":
    main()