import requests
import json

#access token
password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"
projectNameExpected = "TestProject1"
descriptionExpected= "This is the  jacky's first test project"
statusCodeExpected = 200
url = 'http://localhost:8080/api/v3/projects/5'
payload = {"raw":"This is  jacky's first project"}

class Test2:
    def test_get_project_description(self):
        expected_project_name = "TestProject1"
        expected_description = str("his is  jacky's first test project")
        expected_response_status = "200"

        response = requests.get('http://localhost:8080/api/v3/projects/5',
                                auth=(username, password))

        #r=requests.patch(url , payload)
        r = requests.patch["description"](url, payload)

        print("HI JACKY COHEN")


               # "data"= {"This is  jacky's first project"})



        #print('The HTTP Status code is: ', response.status_code)

        # verify status code:
        descriptionActual = json["description"]["raw"]  # verify description
        assert descriptionActual == descriptionExpected, ("Description invalid:", descriptionActual)

        assert response.status_code == statusCodeExpected, ("Get Request Failed, status code:", response.status_code)
        json = response.json()


