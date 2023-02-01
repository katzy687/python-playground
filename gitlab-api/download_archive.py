import requests

url = "http://192.168.85.26/api/v4/projects/quali_natti%2Fterraformstuff/repository/archives?sha=test-branch"

response = requests.get(url, stream=True)
pass
