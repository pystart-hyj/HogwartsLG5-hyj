from appium import webdriver
from homework_appium.page.basepage import BasePage
from homework_appium.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['skipDeviceInitialization'] = 'true'
            caps["ensureWebviewsHavePages"] = True
            caps['settings[waitForIdleTimeout]'] = 1
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)