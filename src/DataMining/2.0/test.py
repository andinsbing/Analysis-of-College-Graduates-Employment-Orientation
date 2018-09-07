from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('http://www.qq.com')
try:
    driver.find_element_by_class_name('totalNum')
except NoSuchElementException as e:
    print(e)

driver.close()
