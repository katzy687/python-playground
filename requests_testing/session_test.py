import requests

base_url = "https://jsonplaceholder.typicode.com"
session = requests.Session()
with session as s:
    s.headers.update({"natti": "hi"})
    r = s.get(base_url + "/posts")
    data = r.json()
print(data)
pass

with session as s:
    r = s.get(base_url + "/posts")
    data = r.json()
print(data)
pass

