# coding=utf-8
from selenium import webdriver


driver = webdriver.Firefox(executable_path=r'C:\Python36\geckodriver.exe')
#driver.get("http://www.baidu.com")

#driver.find_element_by_id("kw").send_keys("selenium2")
#driver.find_element_by_id("su").click()
#driver.quit()

#driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("selenium 2")
#driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("selenium2")
first_url = "http://www.baidu.com"
print("Go %r" %first_url)
driver.get(first_url)

second_url = "http://news.baidu.com"
print("Go %r" %second_url)
driver.get(second_url)

print("back to %r" %first_url)
driver.back()

print("forward to %r" %second_url)
driver.forward()

print("page refresh")
driver.refresh()
