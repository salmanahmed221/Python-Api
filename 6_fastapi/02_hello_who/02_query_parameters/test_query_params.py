import requests

params1 = {"name": "Salman","age": 20}
r = requests.get("http://localhost:8000/hi", params=params1)
print(r.json())