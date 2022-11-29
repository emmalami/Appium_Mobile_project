import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "13",
        "app": "C:/Users/hp/OneDrive/Documents/GitHub/Appium Android Mobile/84272fcb-bc4b-486d-92e8-50c9c515a581.apk",
        "appPackage": "com.payfi.ng.releasestaging",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
