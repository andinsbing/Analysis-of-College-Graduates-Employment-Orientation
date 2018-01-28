from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drive = webdriver.Chrome()
f = open('D:\\科研项目\\target.txt', 'w')
drive.get('https://www.lagou.com')
time.sleep(2)
li = drive.find_elements_by_class_name('menu_box')
for each in li:
    each = each.find_element_by_class_name('menu_sub')
    eachs = each.find_elements_by_tag_name('a')
    for href in eachs:
        f.write("'"+href.get_attribute('href')+"',\n")
f.close()
drive.close()

