
import requests
import json


payload = json.dumps({
  "id": 543212,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2023-10-24T13:39:07.854Z",
  "status": "placed",
  "complete": True
})
headers = {
  'Content-Type': 'application/json'
}
url = "https://petstore.swagger.io/v2/store/order"
response = requests.post(url, headers=headers, data=payload)

print(response.status_code)

