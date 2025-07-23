import requests

url = ('http://127.0.0.1:8000/1.1.1.1.1.-1.0.1.-1.1.1.-1.1.0.-1.-1.1.1.0.1.1.1.1.-1.-1.0.-1.1.1.1')

response = requests.get(url)

print(response)
print(response.text)