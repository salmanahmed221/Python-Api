import requests

params1 = {"name":"salman","password":18}
r = requests.get("http://127.0.0.1:8000/user",params=params1)
print(r.text)