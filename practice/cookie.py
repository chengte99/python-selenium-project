from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.google.com")

driver.add_cookie({'name': 'key-aaaaa', 'value': 'value-aaaaaaaaaaaaa'})
cookies = driver.get_cookies()

for cookie in cookies:
    print("%r -> %r" %(cookie['name'], cookie['value']))

newCookie = driver.get_cookie("key-aaaaa")
print(newCookie)

print("now, delete key-aaaaa cookie")
#driver.delete_cookie("key-aaaaa")
driver.delete_all_cookies()

for cookie in driver.get_cookies():
    if cookie != None:
        print("%r -> %r" %(cookie['name'], cookie['value']))
