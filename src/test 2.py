import requests
import json
#access token
password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"
statusCodeExpected = 200
descriptionExpected= "This is my test project"
url = "http://localhost:8080/api/v3/projects/5/"

class Test2:

    def test_patch_project_description(self):
        expected_project_name = "TestProject1"
        expected_description = str("This is my secound test project")
        expected_response_status = "200"


"description":[

{ "raw"":"This is my 2 test project" }
 ]
print("jacky")
response = requests.get('http://localhost:8080/api/v3/projects/5',
                        auth=(username, password))
assert response.status_code == statusCodeExpected, ("Get Request Failed, status code:", response.status_code)
json = response.json()
print(json)
'''headers = {
  'raw': '"This is Jacky first test project"',
  'Authorization': 'Basic YXBpa2V5OjkwMGNlYjY3YWZjYzM5ODRlODExZTI5ODg5ODA3ZmNhNDk2ZTM3ZTFiOWU0NmY3NWZjODAxNWFiMmVkMjI4MjY=',
  'Content-Type': 'application/json'
}'''
