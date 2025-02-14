from Pages.basePage import BasePage
from selenium.webdriver.common.by import By
from config import configData
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

class HomePage(BasePage):

    def close_welcome_banner(self):
        try:
            self.click_element(By.XPATH, configData.XPATH["close_Welcome_Banner"])
            log.logger.info("Closed the welcome banner.")
        except Exception as e:
            log.logger.error(f"Failed to close welcome banner: {e}")
            raise

    def search_button(self):
        try:
            self.click_element(By.XPATH, configData.XPATH["search_Button"])
            log.logger.info("Clicked on the search button.")
        except Exception as e:
            log.logger.error(f"Failed to click search button: {e}")
            raise

    def search_bar(self):
        try:
            self.click_element(By.XPATH, configData.XPATH["search_Bar"])
            log.logger.info("Clicked on the search bar.")
        except Exception as e:
            log.logger.error(f"Failed to click search bar: {e}")
            raise

    def search_by_text(self):
        try:
            self.send_keys(By.XPATH, configData.XPATH["search_Bar"], configData.TEST_DATA["search_Text"])
            log.logger.info(f"Entered search text: {configData.TEST_DATA['search_Text']}")
        except Exception as e:
            log.logger.error(f"Failed to enter search text: {e}")
            raise

    def search_tab(self):
        try:
            self.click_element(By.XPATH, configData.XPATH["search_Tab"])
            log.logger.info("Clicked on the search tab.")
        except Exception as e:
            log.logger.error(f"Failed to click search tab: {e}")
            raise

    def find_center(self):
        try:
            self.click_element(By.XPATH, configData.XPATH["find_Center"])
            log.logger.info("Clicked on the find center button.")
        except Exception as e:
            log.logger.error(f"Failed to click find center button: {e}")
            raise
