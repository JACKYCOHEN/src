import time
# import pytest
# import self as self
import content as content
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

signin_name = 'jacky21'
signin_user = 'j_cohen_99@yahoo.com'
signin_pass = 'bokertov$300'
#project_description = "My First UI Project"


# def switch_to_last_opened_tab(d):
#     window_handles = d.window_handles
#     d.switch_to.window(window_handles[len(window_handles) - 1])


def find_by_class(d, name):
    return d.find_element_by_class_name(name)


# def test_proj_identifier(name):
#     ret = name.lower()
#     list = ' ,/#@$%'
#     for ch in list:
#         ret = ret.replace(ch, '-')
#     # ret = name.lower().replace(' ','-').replace(',','-').replace('/','-').replace('#','-').replace('@','-').replace('$','-').replace('%','-')
#     return ret


'''project_name = input('Enter project name:')
print('The project name is:', project_name)
identifier_expected = proj_identifier(project_name)
print('The identifier is:', identifier_expected)
project_desc = input('Enter project description')
identifier_actual = identifier_expected
assert identifier_actual == identifier_expected'''

driver = webdriver.Chrome()

# open OpenProject and sign in :
driver.get("https://docs.openproject.org/")
driver.find_element_by_xpath('//a[contains(@href,"signin")]').click()




# enter user name
driver.find_element_by_id('signin-input').send_keys(signin_name)
driver.find_element_by_class_name('button').click()




# enter user and password
driver.find_element_by_id('username').send_keys(signin_user)
driver.find_element_by_id('password').send_keys(signin_pass)
driver.find_element_by_css_selector("#login-form>form>input.button.-highlight").click()

time.sleep(2)
# project page - Click on the "+" button and select "New project":
driver.find_element_by_xpath('//a[contains(@title,"Open quick add menu")]').click()
time.sleep(2)
#driver.find_element_by_xpath('//a[contains(@title,"New Project")]').click()
driver.find_element_by_xpath('//*[@id="quick-add-menu"]/li[1]/a/span').click()

time.sleep(2)


'''project_name = input('Enter project name:')
print('The project name is:', project_name)
identifier_expected = proj_identifier(project_name)
print('The identifier is:', identifier_expected)
project_desc = input('Enter project description')
identifier_actual = identifier_expected
assert identifier_actual == identifier_expected'''
# driver.find_element_by_class_name('op-input').send_keys('Jacky Cohen 1$2@3')


#Step 3 - Enter project name
driver.find_element_by_xpath('//*[@id="formly_3_textInput_name_0"]').send_keys('New Project')

#Step 4 - Enter project description
driver.find_element_by_class_name('op-fieldset--toggle').click()
time.sleep(2)
driver.find_element_by_class_name('op-uc-p').send_keys('My First Project')
time.sleep(2)
#Step 7 - Select status “On track”
driver.find_element_by_xpath('//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input').click()
driver.find_element_by_xpath("//div[./span[.='On track']]").click()

#Step 8 - click On "save” button
time.sleep(2)
driver.find_element_by_xpath("//button[contains(.,'Save')]").click()

time.sleep(5)
#element = driver.find_element_by_xpath("//edit-form[.//p[.="My First Project']]")
element = driver.find_element_by_xpath("//edit-form[contains(.,'My First Project')]")

#assert True

