import json
import time
from urllib import response

import requests



#access token
password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"

projectNameExpected = "TestProject1"
descriptionExpected= "This is my #1 project"
statusCode_POST = 201
statusCode_GET = 200
statusCode_PATCH = 200
statusCode_DELETE = 204
statusCode_NOT_FOUND = 404
id="16"
new_description="This is my first project"
expected_ProjectName = "TestProject_004"
expected_identifier = "testproject-name"
#TEST-001:
# response1 = requests.get(f'http://localhost:8080/api/v3/projects/{id}',auth=(username, password))
# assert response.status_code == "200", ("Get Request Failed, status code:", response.status_code)
# assert response.json()["name"] == projectNameExpected, ("Project name invalid:", response.json()["name"])
# assert response.json()["description"]["raw"]==descriptionExpected , ("Description invalid:", response.json()["description"]["raw"])

#TEST-002
# payload = {'description': {'raw': new_description}}
#
# response2 = requests.patch(f'http://localhost:8080/api/v3/projects/{id}', auth=(username, password), json=payload)
#
# assert new_description == response1.json()["description"]["raw"]
#
# print(new_description,"\n",response1)

#TEST-003-POST

# payload = {
#     "name": "TestProject_Name"
# }
#
# response3 = requests.post(f'http://localhost:8080/api/v3/projects', auth=(username, password), json=payload)
#
# assert statusCode_POST == response3.status_code, ("Get Request Failed, status code:", response3.status_code)
# assert expected_ProjectName == response3.json()["name"]
# print("The new project name is :", response3.json()["name"],"\n","the status code is:",response3.status_code)


#TEST-004-POST

payload = {
    "name": "TestProject_004"
}

response3 = requests.post(f'http://localhost:8080/api/v3/projects', auth=(username, password), json=payload)

assert statusCode_POST == response3.status_code, ("Get Request Failed, status code:", response3.status_code)
assert expected_ProjectName == response3.json()["name"]
print("The new project name is :", response3.json()["name"],"\n","Create project succeeded - the status code is:",response3.status_code)
ID_PROJECT=response3.json()["id"]
print(ID_PROJECT)
time.sleep(10)
#TEST-004-DELETE
response3 = requests.delete(f'http://localhost:8080/api/v3/projects/{ID_PROJECT}', auth=(username, password), json=payload)
assert statusCode_DELETE == response3.status_code, ("Get Request Failed, status code:", response3.status_code)
print("DELETE project  succeeded - The status code is:",response3.status_code)
time.sleep(10)
#GET
response3 = requests.get(f'http://localhost:8080/api/v3/projects/{id}',auth=(username, password))
assert statusCode_NOT_FOUND == response3.status_code, ("Get Request Failed, status code:", response3.status_code)
print("Succeeded!!! Project name not found - the HTTP response status code, is:",response3.status_code)



