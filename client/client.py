import requests


print("Trying to connect...")
response = requests.get('http://127.0.0.1:9999/test')
print(response.text)


response = requests.post('http://127.0.0.1:9999/auth/', json={"name": "admin", "password": "1"})
print(response.text)