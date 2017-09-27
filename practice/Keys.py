from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox(executable_path=r'C:\Python36\geckodriver.exe')
driver.get("https://www.google.com")

driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys("selenium")
driver.find_element_by_xpath("//input[@id='lst-ib']").submit()

sleep(2)
driver.execute_script("window.history.go(-1)")
#driver.back()

sleep(2)
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys("selenium")
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(Keys.CONTROL, 'a')
sleep(2)
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(Keys.CONTROL, 'x')
sleep(2)
driver.find_element_by_xpath("//input[@id='lst-ib']").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_xpath("//input[@id='lst-ib']").submit()
