import config.configData
from config.configData import BROWSER, PAGE_LOAD_TIMEOUT
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from config.configData import BROWSER


class DriverFactory:

    @staticmethod
    def get_driver(browser = BROWSER):
        if browser == "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            raise ValueError(f"This {browser} is not supported, please use Chrome or Firefox")

        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        return driver

