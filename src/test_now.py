import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
signin_name='jacky21'
signin_user='j_cohen_99@yahoo.com'
signin_pass='bokertov$300'

print('test')



def switch_to_last_opened_tab(self):
    window_handles = self.window_handles
    self.switch_to.window(window_handles[len(window_handles) - 1])

def find_by_class(self, name):
    return self.find_element_by_class_name(name)

def proj_identifier(name):
    ret = name.lower()
    list = ' ,/#@$%'
    for ch in list:
        ret = ret.replace(ch,'-')
    #ret = name.lower().replace(' ','-').replace(',','-').replace('/','-').replace('#','-').replace('@','-').replace('$','-').replace('%','-')
    return ret


'''project_name = input('Enter project name:')
print('The project name is:', project_name)
identifier_expected = proj_identifier(project_name)
print('The identifier is:', identifier_expected)
project_desc = input('Enter project description')
identifier_actual = identifier_expected
assert identifier_actual == identifier_expected'''


driver = webdriver.Chrome()
#open web page
driver.get("https://docs.openproject.org/")
driver.find_element_by_xpath('//a[contains(@href,"signin")]').click()
switch_to_last_opened_tab(driver)


#enter user name
driver.find_element_by_id('signin-input').send_keys(signin_name)
driver.find_element_by_class_name('button').click()
switch_to_last_opened_tab(driver)


#enter user and password
driver.find_element_by_id('username').send_keys(signin_user)
driver.find_element_by_id('password').send_keys(signin_pass)
driver.find_element_by_css_selector("#login-form>form>input.button.-highlight").click()

#switch_to_last_opened_tab
switch_to_last_opened_tab(driver)

#project page
driver.find_element_by_xpath('//a[contains(@title,"Open quick add menu")]').click()
driver.find_element_by_xpath('//a[contains(@title,"New project")]').click()
time.sleep(2)


'''project_name = input('Enter project name:')
print('The project name is:', project_name)
identifier_expected = proj_identifier(project_name)
print('The identifier is:', identifier_expected)
project_desc = input('Enter project description')
identifier_actual = identifier_expected
assert identifier_actual == identifier_expected'''

#driver.find_element_by_class_name('op-input').send_keys('Jacky Cohen 1$2@3')

driver.find_element_by_class_name('op-fieldset--toggle').click()
driver.find_element_by_class_name('op-uc-p').send_keys('My First Project')







