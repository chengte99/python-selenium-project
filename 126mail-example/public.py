class Login():

    def user_login(self, driver):
        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='x-URS-iframe']"))
        driver.find_element_by_xpath("//input[@name='email']").clear()
        driver.find_element_by_xpath("//input[@name='email']").send_keys("username")
        driver.find_element_by_xpath("//input[@name='password']").clear()
        driver.find_element_by_xpath("//input[@name='password']").send_keys("password")
        #driver.find_element_by_id("wd").click()

    def user_logout(self, driver):
        driver.find_element_by_id("quit").click()
