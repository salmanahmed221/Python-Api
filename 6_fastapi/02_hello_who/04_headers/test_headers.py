import requests
headers1= {"name" : 'salman'}
r = requests.post("http://localhost:8000/hi", headers=headers1)
print(r.json())