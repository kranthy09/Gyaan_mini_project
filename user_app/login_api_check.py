import requests
import json

url = "  https://9ca80e301882.ngrok.io/api/user_app/login/"
data = {"username":"kranthi", "password":"g"}

headers = {"Content-Type": "application/json"}

req = requests.post(url, json=data, headers=headers)

print(req.content)