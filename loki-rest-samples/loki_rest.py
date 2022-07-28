import json

import requests

url = "http://qs-il-lt-natti:3100/loki/api/v1/query_range"
params = {
    "start": 1650233263396,
    "query": '{job="qualiserver"} |= "ERROR"'
}
response = requests.get(url, params=params)
result_streams = response.json()["data"]["result"]
team_server_data = [x["values"] for x in result_streams if "TeamServer" in x["stream"]["filename"]]
team_server_data = team_server_data[0]
jsonifed = [json.loads(x[1]) for x in team_server_data]
print(json.dumps(jsonifed, indent=4))