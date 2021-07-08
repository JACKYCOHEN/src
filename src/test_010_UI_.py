import time

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

sign_in_name = 'jacky21'
sign_in_user = 'j_cohen_99@yahoo.com'
sign_in_pass = 'bokertov$300'
expected_text = str('New\nTASK')
driver = webdriver.Chrome()

def find_by_class(d, name):
    return d.find_element_by_class_name(name)


# Step # 1 - open OpenProject and sign in :
# -----------------------------------------
def test_login_to_open_project():
    driver.get("https://docs.openproject.org/")
    driver.find_element_by_xpath('//a[contains(@href,"signin")]').click()

    # enter user name
    driver.find_element_by_id('signin-input').send_keys(sign_in_name)
    driver.find_element_by_class_name('button').click()

    time.sleep(2)
    # enter user and password
    driver.find_element_by_id('username').send_keys(sign_in_user)
    driver.find_element_by_id('password').send_keys(sign_in_pass)
    driver.find_element_by_css_selector("#login-form>form>input.button.-highlight").click()
    time.sleep(3)


# Step 2 - On “Home” page, top-left corner, click the “Select a project“ menu button":
# ------------------------------------------------------------------------------------
def test_select_project_from_menu():
    driver.find_element_by_xpath('//*[@id="projects-menu"]/span').click()
    time.sleep(3)
    driver.find_element_by_id("project_autocompletion_input").send_keys("TestProject1")
    time.sleep(3)
    driver.find_element_by_class_name("ui-autocomplete-match").click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="main-menu-work-packages"]/span/span').click()
    time.sleep(2)


def get_menu_link(item_label) -> WebElement:
    return driver.find_element_by_xpath(
        f"//a[./i]/span[.='{item_label}']|" +
        f"//li[./a[.='{item_label}']]|" +
        f"//div[contains(@class,'children-menu-header')]/a[.='{item_label}']")


# Step 3 - COUNT NUMBER OF ROWS IN THE TABLE:
# -------------------------------------------
def test_count_number_of_rows_in_table():
    rows = driver.find_elements_by_xpath("//table//tr[@data-work-package-id]")
    print("Num of rows in table is :", len(rows))
    time.sleep(3)


# Step 4 : Creating new task - Click the “+ create"  green button and select TASK :
# ------------------------------------------------------------------------------
def test_create_new_task():
    driver.find_element_by_class_name("button--text").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="types-context-menu"]/ul/li[1]/a/span').click()
    time.sleep(3)


# Step 5: verify the title of the form is “New TASK”:
# ---------------------------------------------------
def test_verify_the_title():
    title_text = str('New TASK')
    new_element1 = driver.find_element_by_class_name("work-packages--status-selector")
    new_element2 = driver.find_element_by_class_name("work-packages--type-selector")
    assert new_element1.text, new_element2.text == title_text
    print("The Title is :", new_element1.text, new_element2.text)
    #
    time.sleep(2)


# Step 6: Type unique strings into the subject and description boxes:
# -------------------------------------------------------
def test_name_and_description():
    text1 = str('My #1 Task!!! ')
    text2 = str('This is my first (UI)task in "Open Project" (-: ')
    driver.find_element_by_xpath('//*[@id="wp-new-inline-edit--field-subject"]').send_keys(text1)
    time.sleep(2)
    driver.find_element_by_class_name("op-uc-p").send_keys(text2)
    time.sleep(2)


# Step 7 - Click the "save" button:
# ----------------------------------
def test_save_button_click():
    driver.find_element_by_id("work-packages--edit-actions-save").click()


# Step 8 - The number of table rows :
# -----------------------------------
def test_count_the_rows_in_table():
    rows = driver.find_elements_by_xpath("//table//tr[@data-work-package-id]")
    print("Num of rows in table is :", len(rows)+1)
    time.sleep(3)


# Step 9 - Verify the type("TASK") and the subject name, of the last table row:
# -----------------------------------------------------------------------------
def test_type_and_subject_names_in_the_last_row():
    time.sleep(1)
    driver.find_element_by_id("id").click()
    time.sleep(1)
    driver.find_element_by_class_name("menu-item").click()
    time.sleep(3)
    driver.find_element_by_xpath(f"//tbody[1]/tr[1]/td[4]/span/span")
    time.sleep(2)
    # text1 = str("TASK")
    # assert text1 == type.text
    time.sleep(2)
    driver.find_element_by_id("subject").click()
    time.sleep(1)
    driver.find_element_by_class_name("menu-item").click()
    time.sleep(2)
    task_name = driver.find_element_by_xpath(f"//tbody[1]/tr[1]/td[3]/span[2]")
    time.sleep(2)
    text2 = str("My #1 Task!!!")
    assert text2 == task_name.text
    time.sleep(3)
    print("the name of the last row TASK is: ", task_name.text)
    time.sleep(3)
    time.sleep(2)
    print("The end of Test 010 : UI - Create Task")
