import requests

base_url = "https://jsonplaceholder.typicode.com"

with requests.Session() as s:
    r = s.get(base_url + "/posts")
    data = r.json()
x = s
pass

