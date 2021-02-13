from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
# desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['deviceName'] = 'e40a1732'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = 'true'
desired_caps['skipDeviceInitialization'] = 'true'
desired_caps['dontStopAppOnReset'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

# driver.find_element_by_id('home_search').click()
driver.find_element("id",'home_search').click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
sleep(5)
driver.back()
driver.back()
driver.quit()