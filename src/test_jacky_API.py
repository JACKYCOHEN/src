import json
import time
from urllib import response

import requests


#access token
#import username as username

password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"

"Work Package Demo"

expected_work_package_subject = "Task"
new_work_package_subject = " api task 7 "
expected_work_package_description = "_**My Task 1**_"
projectNameExpected = "TestProject-1"
descriptionExpected= "This is my first project after update"
statusCode_POST = 201
statusCode_GET = 200
statusCode_PATCH = 200
statusCode_DELETE = 204
statusCode_NOT_FOUND = 404
expected_status_code_creating = 201
project_id = 24
expected_work_package_id = 5
new_description="This is my first project after update today"
updated_description="This is my api project in python"
expected_ProjectName = "TestProject_Name"
expected_identifier = "testproject-name"


# TEST-001:Get Project by ID
def test_get_project_by_id():
    op_response = requests.get(f'http://localhost:8080/api/v3/projects/{project_id}',auth=(username, password))
    assert op_response.status_code == 200, ("Get Request Failed, status code:", op_response.status_code)
    assert op_response.json()["name"] == projectNameExpected, ("Project name invalid:", op_response.json()["name"])
    assert op_response.json()["description"]["raw"] == descriptionExpected , ("Description invalid:", op_response.json()["description"]["raw"])

def test_Update_project_by_id():
    # TEST-002  - Update(patch) Project
    payload = {'description': {'raw': new_description}}
    op_response = requests.patch(f'http://localhost:8080/api/v3/projects/{project_id}', auth=(username, password), json=payload)
    assert new_description == op_response.json()["description"]["raw"]
    print(new_description,"\n",op_response.text)

    # TEST-003-POST :Create Project
    payload = {
        "name": "TestProject_Name"
    }

    op_response = requests.post(f'http://localhost:8080/api/v3/projects', auth=(username, password), json=payload)

    assert statusCode_POST == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    assert expected_ProjectName == op_response.json()["name"]
    print("The new project name is :", op_response.json()["name"],"\n","the status code is:",op_response.status_code)

    # TEST-004-POST
    payload = {
        "name": "TestProject_004"
    }

    op_response = requests.post(f'http://localhost:8080/api/v3/projects', auth=(username, password), json=payload)

    assert statusCode_POST == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    assert 'TestProject_004' == op_response.json()["name"]

    message = f'The new project name is: {op_response.json()["name"]}\nCreate project succeeded - the status code is: {op_response.status_code}'
    print(message)
    id_project = op_response.json()["id"]
    print(id_project)

    # TEST-004-DELETE
    op_response = requests.delete(f'http://localhost:8080/api/v3/projects/{id_project}', auth=(username, password), json=payload)
    assert statusCode_DELETE == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    print("DELETE project  succeeded - The status code is:",op_response.status_code)
    # GET
    op_response = requests.get(f'http://localhost:8080/api/v3/projects/{id_project}', auth=(username, password))
    assert 404 == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    print("Succeeded!!! Project name not found - the HTTP response status code, is:",op_response.status_code)


# TEST-005-Get Work Package by ID:
def test_get():
    response = requests.get(f'http://localhost:8080/api/v3/work_packages/38', auth=(username, password))
    assert response.status_code == 200, ("Get Request Failed, status code:", response.status_code)
    assert response.json()["subject"] == 'Work Package Demo', ("Project name invalid:", response.json()["elements"]["subject"])
    assert response.json()["description"]["raw"] == 'Exc 10', ("Description invalid:", response.json()["description"]["raw"])
    print("success")


    # TEST-006  - Update(patch) Work Package:
def test_patch():
    response = requests.get(f'http://localhost:8080/api/v3/work_packages/{expected_work_package_id}', auth=(username, password))
    current_lockVersion = str(response.json()["lockVersion"])
    payload ={"lockVersion": current_lockVersion, "description": {"raw": new_description}}
    op_response = requests.patch(f'http://localhost:8080/api/v3/work_packages/{expected_work_package_id}', auth=(username, password), json=payload)
    assert new_description == op_response.json()["description"]["raw"]
    print(new_description,"\n",op_response.text)


    # TEST-007  - Create Work Package:
def test_create_new_work_package():
    payload = { "subject": "My Package" }
    op_response = requests.post('http://localhost:8080/api/v3/projects/1/work_packages', auth=(username, password), json=payload)
    assert 'My Package' == op_response.json()["subject"]
    print(new_work_package_subject,"\n",op_response.text)

    # + str(expected_work_package_id)


    # TEST-008  -
def test_delete_work_package_id():
    payload = { "subject": "My Package" }
    op_response = requests.post('http://localhost:8080/api/v3/projects/1/work_packages', auth=(username, password), json=payload)
    assert op_response.status_code == 201
    package_id = op_response.json()['id']

    headers = {
        "Content-Type": "application/json"
    }
    op_response = requests.delete(f'http://localhost:8080/api/v3/work_packages/{package_id}', auth=(username, password), headers=headers)
    assert op_response.status_code == 204

    op_response = requests.get(f'http://localhost:8080/api/v3/work_packages/{package_id}', auth=(username, password), headers=headers)
    assert op_response.status_code == 404
