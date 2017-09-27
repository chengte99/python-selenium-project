from selenium import webdriver
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')
