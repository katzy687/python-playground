import requests
url = "https://raw.githubusercontent.com/nahumtimerman/udemyApp/master/mazeService/Cell.cs"
token = "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"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get(url, stream=True, headers=headers, verify=False)
pass