import requests
import json

url = "http://127.0.0.1:8000/api/gyaan/get/user/domains/"
data = {"username":"kranthi", "password":"kranthi"}

headers = {"Content-Type": "application/json", "Authorization": "Bearer token"}

req = requests.get(url, headers=headers)

print(req.content)