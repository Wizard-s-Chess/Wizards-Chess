import requests

def capture():
    url = "http://192.168.4.1/capture"
    req = requests.get(url)
    with open("chess.jpg", 'wb') as f:
        f.write(req.content)