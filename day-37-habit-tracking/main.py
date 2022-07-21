import requests
from datetime import datetime


USERNAME = "abhi29"
TOKEN = "Abhishek@2900"
GRAPH_NAME = "Coding Graph"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


# Create a user
user_obj = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_obj)
# print(response.text)


# Create a graph
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_body = {
    "id": "graph-1",
    "name": GRAPH_NAME,
    "unit": "commit",
    "type": "int",
    "color": "ichou",
    "timezone": "Asia/Kolkata"
}
# response = requests.post(url=graph_endpoint, json=graph_body, headers=headers)
# print(response.text)


# Post a pixel
pixel_body = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "1",
}
response = requests.post(url=f"{graph_endpoint}/graph-1", json=pixel_body, headers=headers)
print(response.text)

