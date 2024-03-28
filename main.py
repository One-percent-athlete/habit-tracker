import requests
import datetime as dt
import os 
import dotenv
dotenv.load_dotenv()

username = os.environ.get("username")
token = os.environ.get("token")
pixela_endpoint="https://pixe.la/v1/users"
graph_endpoint=f"{pixela_endpoint}/{username}/graphs"
graph_id="graph0"

params = {
    "token":token,
    "username":username, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}
res = requests.post(url=pixela_endpoint, json=params)
print(res)

graph_config = {
    "id":"graph0",
    "name":"one-percent",
    "unit":"commit",
    "type":"int",
    "color":"kuro",
}

headers = {
 "X-USER-TOKEN":token
}

today = dt.datetime.now().strftime("%Y%m%d")

pixal_config={
    "date":"20240306",
    "quantity":"10"
}
res = requests.post(url=graph_endpoint,headers=headers,json=graph_config)
print(res.text)

res = requests.post(url=f"{graph_endpoint}/{graph_id}",headers=headers,json=pixal_config)
print(res.text)

pixal_config={
    "quantity":"12"
}

res = requests.put(url=f"{graph_endpoint}/{graph_id}/{today}", headers=headers,json=pixal_config)

print(res.text)

res = requests.delete(url=f"{graph_endpoint}/{graph_id}/20240306", headers=headers)
print(res.text)