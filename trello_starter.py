# This code takes the Trello API key and token from the config_starter.yaml file and uses it to search for a board named 'abc_board' abd produce the boare_kd
# The original trello spec in the synapse copilot repo does not allow of deleting a board by name.
# http://docs.python-requests.org
import requests
import json
import sys
import os
from dotenv import load_dotenv
import logging

import yaml

logging.basicConfig(
    format="%(message)s",
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

url = "https://api.trello.com/1/search"
config = yaml.load(open("config_starter.yaml", "r"), Loader=yaml.FullLoader)

# check to see if the configuration file is being used
if config is None:
    logger.error("Could not load configuration file")
    sys.exit(1)
else:
    logger.info("Configuration file loaded successfully")

if config["use_config_file"] is True:
    # iterate through the config file and set the environment variables
    for key, value in config.items():
      os.environ[key.upper()] = str(value)
    logger.info("Environment variables set successfully")
else:
    logger.info("Skipping configuration file")
    # Load environment variables from .env file
    load_dotenv()

headers = {
  "Accept": "application/json"
}

query = {
  'query': 'abc_board',
  'key': os.getenv("TRELLO_API_KEY"),
  'token': os.getenv("TRELLO_TOKEN")
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

# Assuming `response` is the result of a request made with the requests library
if response.status_code == 200:
  try:
      response_json = json.loads(response.text)
      print(json.dumps(response_json, sort_keys=True, indent=4, separators=(",", ": ")))
  except json.JSONDecodeError:
      print("Failed to decode JSON from response. Response content:", response.text)
else:
  print(f"Request failed with status code {response.status_code}: {response.text}")