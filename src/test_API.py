import requests
import json

#access token
 # from tests_api.test_002 import payload

password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"
projectNameExpected = "TestProject1"
descriptionExpected= "This is my first project"
statusCodeExpected = 200


class Test2:

  def test_get_project_id(self):
    expected_project_name = "TestProject1"
    expected_description = str("This is my #1 project")

    response = requests.get('http://localhost:8080/api/v3/projects/5',auth=(username, password))
    print(f"The code is: {response.status_code}")
    assert response.status_code == 200


  def test_update_projects_description(self):
    url = "http://localhost:8080/api/v3/projects/5"

   payload = json.dumps({
      "description": {
        "raw": "This is my #1 project"
      }
    })
  headers = {
      'raw': "This is my #1 project",
      'Authorization': 'Basic YXBpa2V5OjkwMGNlYjY3YWZjYzM5ODRlODExZTI5ODg5ODA3ZmNhNDk2ZTM3ZTFiOWU0NmY3NWZjODAxNWFiMmVkMjI4MjY=',
      'Content-Type': 'application/json'
    }
    # response = requests.patch(url, headers=headers, data=payload)
    response = requests.request("PATCH",  data=payload,auth=(username, password))
    print(f"The status code {response.status_code}")
    print(response.text)

    # assert response.status_code == statusCodeExpected, ("Get Request Failed, status code:", response.status_code)
    #print(response.json())
    #projectNameActual = json.["name"]  # verify project name

    #print(projectNameActual)
    '''assert projectNameActual == projectNameExpected, ("Project name invalid:", projectNameActual)
    descriptionActual = json["description"]["raw"]  # verify description
    assert descriptionActual == descriptionExpected, ("Description invalid:", descriptionActual)
    #print("the status code is:",response.status_code)
    #print("the project name is:" ,projectNameActual)'''
