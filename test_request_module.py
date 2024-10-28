import requests

url = "https://postman-echo.com/post"

payload = "hello DevNet"

headers = {'content-type': "text/plain"}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)