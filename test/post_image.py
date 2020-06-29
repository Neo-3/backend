import requests
import json

url = 'http://localhost:5000/api/v1/classifier'
myimg = ({'image': open("medidor.jpg", "rb")})

x = requests.post(url, files = myimg)

print(x.json())