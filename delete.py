import requests
import json

url = "https://reqres.in/api/users"

payload={}
headers={}
users_data = requests.request("GET", url, headers=headers, data=payload)

x = json.loads(users_data.text)

# Verificar si hay datos de usuario
if "data" in x:
    # Obtener el usuario que quieres eliminar, por ejemplo, el quinto usuario (índice 4)
    user_to_eliminar = x["data"][5]

    # Obtener el ID del usuario a eliminar
    user_id = user_to_eliminar["id"]

    # Construir la URL específica del usuario a eliminar
    delete_url = f"{url}/{user_id}"

    # Enviar la solicitud DELETE a la URL específica del usuario
    response = requests.delete(delete_url)

    # Verificar el código de estado de la respuesta DELETE
    if response.status_code == 204:
        print(f"El usuario {user_to_eliminar['first_name']} se ha eliminado correctamente.")

    else:
        print(f"Error al eliminar el usuario. Código de estado: {response.status_code}")

