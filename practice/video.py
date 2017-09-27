from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://videojs.com")

video = driver.find_element_by_xpath("//video[@id='preview-player_html5_api']")

url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

print("start")
driver.execute_script("return arguments[0].play()", video)

sleep(10)

print("stop")
driver.execute_script("return arguments[0].pause()", video)

print("screenshot")
driver.get_screenshot_as_file("C:\\Users\\chengte.lin\\Desktop\\Python Project\\screenshot.jpg")
