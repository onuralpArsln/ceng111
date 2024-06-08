import requests

response = requests.get("http://127.0.0.1:8000")
#this adress is got by running uvicorn <file_name>:<app_name> --reload
# it starts your fast api server app 



response = requests.get("http://127.0.0.1:8000/items/2")

response = requests.get("http://127.0.0.1:8000/items?name=Nails")

response = requests.get("http://127.0.0.1:8000/hackername")

print(response.status_code)
print(response.json())
