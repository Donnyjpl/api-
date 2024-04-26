import requests
import json

url = "https://reqres.in/api/users/2"
updated_user={
    "name": "morpheus",
    "job": "zion resident"
}
payload =updated_user
headers = {'Content-Type': 'application/json'}

# Convertir el diccionario payload a una cadena JSON
json_payload = json.dumps(payload)

response = requests.put(url, headers=headers, data=json_payload)

print(response)
print(response.text)