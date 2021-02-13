from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.sse.android.listcompanykcb.pre'
        desired_caps['appActivity'] = 'com.sse.structure.ui.Splash.SplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        sleep(2)
        action = TouchAction(self.driver)
        action.press(x=190,y=453).wait(100).move_to(x=286,y=453).wait(100).move_to(x=380,y=453).wait(100).\
                     move_to(x=380,y=549).wait(100).move_to(x=380,y=645).release().perform()
        sleep(2)
