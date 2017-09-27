# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()

driver.find_element_by_link_text("搜索设置").click()
time.sleep(2)

driver.find_element_by_link_text("保存设置").click()
time.sleep(2)

alert_message = driver.switch_to_alert().text
print(alert_message)
driver.switch_to_alert().dismiss()
