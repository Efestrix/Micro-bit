import requests

start_url = "http://localhost:8080"
next_url = start_url

while True:
    next_url = requests.get(next_url).text
    print(next_url)
