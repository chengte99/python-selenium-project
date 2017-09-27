from selenium import webdriver

#driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver = webdriver.Ie(executable_path=r'C:\Python36\IEDriverServer.exe')

#driver.get("http://www.126.com")
driver.get("http://www.baidu.com")

# 正常可以取得id, name 的屬性
#driver.switch_to.frame(driver.find_element_by_id('x-URS-iframe'))
# 也可以用XPATH取得
driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='x-URS-iframe']"))


driver.find_element_by_xpath("//input[@name='email']").clear()
driver.find_element_by_xpath("//input[@name='email']").send_keys("username")
#driver.find_element_by_xpath("//input[@name='password']").clear()
#driver.find_element_by_xpath("//input[@name='password']").send_keys("password")
#driver.find_element_by_xpath("//a[@class='forgetpwd j-redirect']").click()
