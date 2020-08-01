import requests
import json

url = "http://127.0.0.1:8000/api/user_app/login/"
data = {"username":"kranthi", "password": "kranthi"}

headers = {"Content-Type": "application/json"}

req = requests.post(url, json=data, headers=headers)

print(req.content)
# , "Authorization": "Bearer token"