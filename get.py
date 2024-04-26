import requests
import json
url = "https://reqres.in/api/users"
payload={}
headers={}
users_data = requests.request("GET", url, headers=headers, data=payload)
x=json.loads(users_data.text)
print(x)


