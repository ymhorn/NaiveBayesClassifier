import requests

url = ('http://127.0.0.1:8000/senior.low.maybe.excellent')

response = requests.get(url)

print(response)
print(response.text)