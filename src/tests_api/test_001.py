import requests
import pytest


#access token
password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"
projectNameExpected = "TestProject1"
descriptionExpected= "This is my #1 project"
statusCodeExpected = 200

# comment
class Test1:

    def test_get_project_id(self):
        expected_project_name = "TestProject1"
        expected_description = str("This is my #1 project")
        expected_response_status = "200"

        response = requests.get('http://localhost:8080/api/v3/projects/5',
                                auth=(username, password))
        #print('JACKY', response.status_code)
        # verify status code
        assert response.status_code == statusCodeExpected, ("Get Request Failed, status code:", response.status_code)
        json = response.json()
        projectNameActual = json['name'] # verify project name
        assert projectNameActual == projectNameExpected, ("Project name invalid:", projectNameActual)
        descriptionActual = json["description"]["raw"]  # verify description
        assert descriptionActual == descriptionExpected, ("Description invalid:", descriptionActual)
        print("\nThe actual project name is :", projectNameActual)
