# This code takes the Trello API key and token from the config_starter.yaml file and uses it to search for a board named 'abc_board' abd produce the boare_kd
# The original trello spec in the synapse copilot repo does not allow of deleting a board by name.
# http://docs.python-requests.org
import requests
import json

import yaml

url = "https://api.trello.com/1/search"
config = yaml.load(open("config_starter.yaml", "r"), Loader=yaml.FullLoader)

headers = {
  "Accept": "application/json"
}

query = {
  'query': 'abc_board',
  'key': config["trello_api_key"],
  'token': config["trello_token"]
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))