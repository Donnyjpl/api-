import requests
import json

url = "https://reqres.in/api/users"
created_user = {"nombre":"Ignacio", "trabajo":"Profesor"}
payload =created_user
headers = {'Content-Type': 'application/json'}

# Convertir el diccionario payload a una cadena JSON
json_payload = json.dumps(payload)

response = requests.post(url, headers=headers, data=json_payload)

print(response)
print(response.text)