import requests
paylod= {"name" : 'salman'}
r = requests.post("http://localhost:8000/hi", json=paylod)
print(r.json())