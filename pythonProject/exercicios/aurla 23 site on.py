import requests
while True:
    url = "https://www.youtube.com"
    if requests.get(url).status_code == 200:
        print("O servidor está disponível.")
        print(requests.get(url).status_code)
    else:
        print("O servidor está indisponível.")