import requests

url = "https://github.com/miskatul-anwar"
response = requests.get(url)
statuscode = response.status_code
print(statuscode)
type(response)
