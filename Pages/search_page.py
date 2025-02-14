import logging

from Pages.basePage import BasePage
from selenium.webdriver.common.by import By
from config import configData
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class SearchPage(BasePage):

    def get_text(self):
        """Retrieves text from a specified element."""
        try:
            element = self.get_element(By.XPATH, configData.XPATH["get_Text"])
            text = element.text
            log.logger.info(f"Retrieved text: {text}")
            return text
        except Exception as e:
            log.logger.error(f"Failed to retrieve text: {e}")
            raise
