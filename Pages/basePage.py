import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.LogUtil import Logger
from config.configData import WAIT

log = Logger(__name__, logging.INFO)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT)
        log.logger.info("BasePage initialized with WebDriver")

    def click_element(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            log.logger.info(f"Clicked on element: {value}")
        except Exception as e:
            log.logger.error(f"Failed to click element {value}: {e}")
            raise

    def send_keys(self, by, value, text):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            element.send_keys(text)
            log.logger.info(f"Entered text '{text}' into element: {value}")
        except Exception as e:
            log.logger.error(f"Failed to enter text into element {value}: {e}")
            raise
        time.sleep(2)  # Reduce unnecessary wait

    def get_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            log.logger.info(f"Element found: {value}")
            return element
        except Exception as e:
            log.logger.error(f"Failed to locate element {value}: {e}")
            raise

    def enter_key(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            element.send_keys(Keys.ENTER)
            log.logger.info(f"Pressed ENTER key on element: {value}")
            return element
        except Exception as e:
            log.logger.error(f"Failed to press ENTER on element {value}: {e}")
            raise

    def get_all_elements(self, by, value):
        try:
            time.sleep(8)
            elements = self.wait.until(EC.presence_of_all_elements_located((by, value)))
            log.logger.info(f"Found {len(elements)} elements for locator: {value}")
            return elements
        except Exception as e:
            log.logger.error(f"Failed to locate elements {value}: {e}")
            raise
