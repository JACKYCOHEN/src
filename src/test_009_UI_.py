import time
from selenium import webdriver

sign_in_name = 'admin'
sign_in_user = 'j_cohen_99@yahoo.com'
sign_in_pass = 'bokertov$300'
expected_text = str('New\nTASK')
driver = webdriver.Chrome()
project_name = "Hello World"


def find_by_class(d, name):
    return d.find_element_by_class_name(name)

# Step 1 -Login to OpenProject:


def test_login_to_open_project():
    driver.get("http://localhost:8080/")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wrapper"]/header/div[3]/ul/li[3]/a/span').click()
    time.sleep(3)

    # enter user name
    driver.find_element_by_xpath('//*[@id="username-pulldown"]').send_keys(sign_in_name)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password-pulldown"]').send_keys(sign_in_pass)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="login-pulldown"]').click()
    time.sleep(1)

# Step 2 - project page - Click on the "+" button and select "New project":


def test_select_new_project():
    driver.find_element_by_xpath('//a[contains(@title,"Open quick add menu")]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="quick-add-menu"]/li[1]/a/span').click()
    time.sleep(2)


'''project_name = input('Enter project name:')
print('The project name is:', project_name)
identifier_expected = proj_identifier(project_name)
print('The identifier is:', identifier_expected)
project_desc = input('Enter project description')
identifier_actual = identifier_expected
assert identifier_actual == identifier_expected
driver.find_element_by_class_name('op-input').send_keys('Jacky Cohen 1$2@3')'''


# Step 3 - Enter project name

def test_enter_project_name():
    driver.find_element_by_xpath('//*[@id="formly_3_textInput_name_0"]').send_keys("Hello World")
    time.sleep(2)


# Step 4 - Click “ADVANCED SETTINGS” title

def test_advanced_settings():
    driver.find_element_by_class_name('op-fieldset--toggle').click()
    time.sleep(2)


# Step 5 - Type some text to the description text box:

def test_project_description():
    driver.find_element_by_class_name('op-uc-p').send_keys('My First Project')
    time.sleep(3)


# Step 7 - Select status “On track”

def test_status_on_track():

    driver.find_element_by_xpath('//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div').click()

#   driver.find_element_by_xpath('//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input').click()
    time.sleep(2)
    driver.find_element_by_class_name("-on-track").click()

# Step 8 - click On "save” button


def test_click_save_button():
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(.,'Save')]").click()
    time.sleep(2)


# Step 9 - Verify the project name
def test_verify_project_name():
#   project_name = "project_name"
    element = driver.find_element_by_xpath('//*[@id="projects-menu"]/span')
    time.sleep(2)
    assert project_name == element.text
    print("The new project name is:", element.text)
