from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

driver.set_window_size(600, 600)

driver.find_element_by_id("kw").send_keys("selenium 2")

sleep(2)
#driver.execute_script("window.scrollTo(100, 450);")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
