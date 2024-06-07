import requests

response = requests.get("https://nervous-sunbonnet-crab.cyclic.app/")

print(response.status_code)
print(response.json())

