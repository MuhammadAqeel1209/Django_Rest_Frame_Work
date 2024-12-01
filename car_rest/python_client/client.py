import requests

endPoints = "http://127.0.0.1:8000/car/list"

data = requests.get(endPoints)
print(data.json())
print(data.status_code)