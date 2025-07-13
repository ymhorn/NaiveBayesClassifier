import requests

url = ('http://127.0.0.1:8000/senior.high.0.fair')

response = requests.get(url)

print(response)
print(response.json())