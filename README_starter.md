# **Synapse Copilot Starter Kit**

This is an unofficial starter kit for the Synapse Copilot project. The Synapse Copilot is a tool that allows you to integrate Large Language Models (LLMs) with a wide array of APIs. 

This starter kit is a fork of the original official repo at [https://github.com/Agile-Loop/Synapse-Copilot.git](https://github.com/Agile-Loop/Synapse-Copilot.git). It does not overwrite the original repository files and all additional files has a *_starter* prefix in the filename.

The intention is to provide a quick starting point to follow along the YouTube video [Synapse Copilot Starter Tutorial](https://youtu.be/_ilJAjcGjvM) that helps you to quickly understand the project structure by running an example scenario and later on perhaps a way to create your own scenario.

## **Additional Files**
Presently the following files are additionally included.


| File Name           | Description                                                                                                  |
|---------------------|--------------------------------------------------------------------------------------------------------------|
| README_starter.md   | This file contains the starter kit information.                                                               |
| config_starter.yaml | Copy of the original config.yaml but trimmed down to only include the keys required for the starter kit.    |
| trello_starter.py   | Convenience script to search for boards in Trello by name.                                                    |
| run_starter.py      | A version of run_py that has been cleaned up to prevent confusion and to make it easier to understand.      |

# **Quick Start Running The Example Trello Scenario**

You can watch the YouTube video at [Synapse Copilot Starter Tutorial](https://www.youtube.com/watch?v=3Q6J9Q1Q9ZQ) for a quick start guide or follow the instructions

Kickstart your journey by cloning the *forked* GitHub repository and installing the required dependencies:

```bash
git clone https://github.com/goldzulu/Synapse-Copilot.git
cd Synapse-Copilot
pip install –r requirements.txt
```

## **Step 1: Grab your OPENAI or AZURE OPENAI keys**

1. Create an OpenAI or Azure OpenAI account and obtain your API keys OpenAI [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) or 
Azure [https://www.c-sharpcorner.com/article/how-to-get-azure-open-ai-keys-and-endpoint/](https://www.c-sharpcorner.com/article/how-to-get-azure-open-ai-keys-and-endpoint/).

2. Open ```config_starter.yaml``` and replace the placeholder with your OpenAI API key. Make sure the ```use_config_file``` is set to ```true``` to use values
from this file. 

```yaml
openai_api_key: "your_openai_api_key"
```

```yaml
AZURE_OPENAI_API_VERSION: "2023-05-15"
AZURE_OPENAI_ENDPOINT: "https://AZURE_RESOURCE.openai.azure.com"
AZURE_OPENAI_API_KEY: "your_azure_openai_api_key"
AZURE_OPENAI_DEPLOYMENT_NAME: "GPT4"
```

3. Alternatively, I've also added a way to use .env files instead, if you like to use .env file, just copy .env.local to .env and then fill up the keys for this
and subsequent settings needed. Make sure ```config_starter.yaml``` ```use_config_file``` is set to ```false```.

## **Step 2: Grab your Trello API key and token**

1. The first thing you'll need to do is either login to your Trello 
account or create a new account.

2. Create a workspace if not already. Remember the name given to the workspace.

3. Next, you would need a PowerUp. Go to the Power-Up Admin Portal [https://trello.com/power-ups/admin](https://trello.com/power-ups/admin).

4. Create a Power Up for the workspace you want to use. Name it whatever you want.

5. Go to the API section if not already, copy the API key once created and keep it safe.

6. Since this is just used by you, you just need to manually generate a token for local testing by following the token link in the API section. Copy the token and keep it safe.

7. Open config_starter.yaml in the root of the project and replace the placeholders.

```yaml
trello_api_key: "your_trello_api_key"
trello_token: "your_trello_token"
```

## **Step 3: Run the starter script**

Now you are ready to run the example by typing:

```bash
python run_starter.py
```

NOTE: A few UserWarnings might come out regarding langchain, but you can ignore them. Probably AgileLoop will fix that at some point but it involves changing so of the code in the repository.

Once run you should see:

```
Please select a scenario (trello/tmdb):
```

Type ```trello``` and hit enter.

When asked:

```
Example instruction: Create a new board with name 'abc_board'

Please input an instruction (Press ENTER to use the example instruction):
```

Just hit enter to use the example instruction.

The Synapse Copilot will then do its magic and if all goes well, you should see the output in the terminal.

```
Parser: The newly created board has the ID "6673f4a370ff71e0981ffd19" and is named "abc_board".
Caller: Thought: I have successfully executed the plan to create a new board on Trello and received the response with the board's ID and name.

Execution Result: Successfully created a new board on Trello named 'abc_board'. The ID of the newly created board is 6673f4a370ff71e0981ffd19.
Planner: Thought: I have finished the execution plan and created a board named 'abc_board'.
Final Answer: I have created a board named 'abc_board'.
Execution Time: 21.642616033554077
```

Take note of the board ID and name as you will need it for the next steps.

## **Step 4: Verify the board creation**

1. Go back to your trello workspace and verify that the board abc_board has been created.

2. You can also verify the board ID by running the trello_starter.py script and searching for the board by name. If you have used abc_board, you can simply just run the script.

```bash
python trello_starter.py
```

You should see something like:

```json
{
    "boards": [
        {
            "id": "6673f4a370ff71e0981ffd19",
            "idOrganization": "6673cbe01472f49befcdb6e4",
            "name": "abc_board"
        }
    ],
    ...
}
```

## **Step 5: Celebrate!**

1. Congrats! You have successfully run the example scenario.

2. You can now go further if you want and rerun ```run_starter.py``` to delete the board with the id that you have copied above.

## Next Steps
Watch the YouTube video [Synapse Copilot Starter Tutorial](https://youtu.be/_ilJAjcGjvM) if not already as i go through the code and explain a bit deeper on how things work.

This starter kit is created as part of a LabLab.ai hackathon. I will be adding more scenarios and features to this starter kit after the hackathon once I backport some of the hackathon code to this repository.

More videos coming soon.

Please open up a github issue to this repository or put some comments on the YouTube video and let me know what you think.

You can also follow me on X at [@voicetechguy1](https://x.com/voicetechguy1).