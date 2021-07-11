import time
import requests
# import username as username
# import password as password

password = "900ceb67afcc3984e811e29889807fca496e37e1b9e46f75fc8015ab2ed22826"
username = "apikey"

"Work Package Demo"
statusCode_POST = 201
statusCode_GET = 200
statusCode_PATCH = 200
statusCode_DELETE = 204
statusCode_NOT_FOUND = 404
expected_status_code_creating = 201

proj_step1_id = 102
project_id = 77
work_package_ID = 73

expected_work_package_id = 5
step_1_project_name = "TestProject_1"
step_1_proj_desc = "This is the first test project"

project_Name_Expected = "TestProject1"
exist_proj_description = "This is the first test project"
new_proj_description = "This is my first project after update today"
expected_ProjectName1 = "TestProject_New"
exist_task_description = '**Exc 005**'
updated_task_description = "Exc 006"
exist_work_package_description = "My Task 1"
new_work_package1 = "Task 007"
new_work_package2 = "Task 008"

expected_identifier = "testproject-name"


def test_get_project_by_id():
    # TEST-001:Get Project by ID
    op_response = requests.get(f'http://localhost:8080/api/v3/projects/{proj_step1_id}', auth=(username, password))
    assert op_response.status_code == statusCode_GET, ("Get Request Failed, status code:", op_response.status_code)
    assert op_response.json()["name"] == step_1_project_name, ("Project name invalid:", op_response.json()["name"])
    assert op_response.json()["description"]["raw"] == step_1_proj_desc, (
    "Description invalid:", op_response.json()["description"]["raw"])
    print("The exist project name is :", op_response.json()["name"])
    print("The exist project description is :", op_response.json()["description"]["raw"])




def test_Update_project_by_id():
    # TEST-002  - Update(patch) Project
    payload = {'description': {'raw': new_proj_description}}
    op_response = requests.patch(f'http://localhost:8080/api/v3/projects/{project_id}', auth=(username, password),
                                 json=payload)
    time.sleep(2)
    assert new_proj_description == op_response.json()["description"]["raw"]
    # print(new_proj_description,"\n",op_response.text)
    print("The project name after update is :", op_response.json()["description"]["raw"], "\n", "the status code is:",
          op_response.status_code)


# op_response.json()["name"]

def test_Create_Project():
    # TEST-003-POST :Create Project
    payload = {
        "name": "TestProject_New"
    }

    op_response = requests.post(f'http://localhost:8080/api/v3/projects', auth=(username, password), json=payload)

    assert statusCode_POST == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    assert expected_ProjectName1 == op_response.json()["name"]
    print("The new project name is :", op_response.json()["name"], "\n", "the status code is:", op_response.status_code)


def test_create_and_delete_Project():
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
    op_response = requests.delete(f'http://localhost:8080/api/v3/projects/{id_project}', auth=(username, password),
                                  json=payload)
    assert statusCode_DELETE == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    print("DELETE project  succeeded - The status code is:", op_response.status_code)
    time.sleep(5)
    # GET
    op_response = requests.get(f'http://localhost:8080/api/v3/projects/{id_project}', auth=(username, password))
    assert statusCode_NOT_FOUND == op_response.status_code, ("Get Request Failed, status code:", op_response.status_code)
    print("Succeeded!!! Project name does not exist any more. The HTTP response status code, is:", op_response.status_code)


# TEST-005-Get Work Package by ID:
def test_get():
    response = requests.get(f'http://localhost:8080/api/v3/work_packages/{work_package_ID}', auth=(username, password))
    assert response.status_code == statusCode_GET, ("Get Request Failed, status code:", response.status_code)
    assert response.json()["subject"] == exist_work_package_description, (
    "Project name invalid:", response.json()["elements"]["subject"])
    assert response.json()["description"]["raw"] == exist_task_description, (
    "Description invalid:", response.json()["description"]["raw"])

def test_update_Work_Package_description():
    # TEST-006  - Update(patch) Work Package description:
    response = requests.get(f'http://localhost:8080/api/v3/work_packages/{expected_work_package_id}',
                            auth=(username, password))
    current_lockVersion = str(response.json()["lockVersion"])
    payload = {"lockVersion": current_lockVersion, "description": {"raw": updated_task_description}}
    op_response = requests.patch(f'http://localhost:8080/api/v3/work_packages/{expected_work_package_id}',
                                 auth=(username, password), json=payload)
    assert updated_task_description == op_response.json()["description"]["raw"]
    print("The updated_task_description is:", op_response.json()["description"]["raw"])

    # TEST-007  - Create Work Package:
def test_create_new_work_package():
    # TEST-007  - Create Work Package:
    payload = {"subject": new_work_package1}
    op_response = requests.post('http://localhost:8080/api/v3/projects/1/work_packages', auth=(username, password),
                                json=payload)
    assert new_work_package1 == op_response.json()["subject"]
    print("The new_work_package_subject is:", op_response.text)


def test_delete_work_package_id():
    # TEST-008  -create new work package (task):
    payload = {"subject": new_work_package2}
    op_response = requests.post('http://localhost:8080/api/v3/projects/1/work_packages', auth=(username, password),
                                json=payload)
    assert new_work_package2 == op_response.json()["subject"]
    assert op_response.status_code == statusCode_POST
    package_id = op_response.json()['id']

    headers = {
        "Content-Type": "application/json"
    }

    # delete new work package (task):
    op_response = requests.delete(f'http://localhost:8080/api/v3/work_packages/{package_id}', auth=(username, password),
                                  headers=headers)
    assert op_response.status_code == statusCode_DELETE
    print("Task successfully Deleted - the status code is :", op_response.status_code )

    op_response = requests.get(f'http://localhost:8080/api/v3/work_packages/{package_id}', auth=(username, password),
                               headers=headers)

    assert op_response.status_code == statusCode_NOT_FOUND
    print("Success - new_work_package2 does not exist any more !!! The status code is : ",op_response.status_code )
    print("\n TEST api has finished - All steps passed : great job!!!")
