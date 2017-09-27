from selenium import webdriver
import os, time

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")

for item in checkboxs:
    item.click()
    time.sleep(1)

num = len(checkboxs)
print(num)

driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()
