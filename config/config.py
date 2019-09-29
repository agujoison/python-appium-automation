import os

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Config:

    @staticmethod
    def get_desirable_capabilities():
        return {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'Android Emulator',
            'app': PATH('../apps/ApiDemos-debug.apk')
        }

    @staticmethod
    def get_driver():
        return webdriver.Remote('http://localhost:4723/wd/hub', Config.get_desirable_capabilities())
