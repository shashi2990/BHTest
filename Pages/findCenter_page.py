import time

from Pages.basePage import BasePage
from selenium.webdriver.common.by import By
from config import configData
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class FindCenterPage(BasePage):

    def search_bar_on_centerpage(self):
        try:
            self.send_keys(By.XPATH, configData.XPATH["serach_Bar_On_CenterPage"], configData.TEST_DATA["city"])
            log.logger.info("Entered city name in search bar")
        except Exception as e:
            log.logger.error(f"Failed to enter city name in search bar: {e}")
            raise

    def enter_key_on_searchBar(self):
        try:
            self.enter_key(By.XPATH, configData.XPATH["enter_Key_On_SearchBar"])
            time.sleep(8)
            log.logger.info("Pressed ENTER on search bar")
        except Exception as e:
            log.logger.error(f"Failed to press ENTER on search bar: {e}")
            raise

    def final_count(self):
        try:
            count_element = self.get_element(By.XPATH, configData.XPATH["final_Count"])
            total_count = count_element.text
            log.logger.info(f"Final search count: {total_count}")
            return total_count
        except Exception as e:
            log.logger.error(f"Failed to get final count: {e}")
            raise

    def get_all_counts(self):
        try:
            time.sleep(8)
            all_elements = self.get_all_elements(By.XPATH, configData.XPATH["get_All_Counts"])
            count = len(all_elements)
            log.logger.info(f"Total search results found: {count}")
            return count
        except Exception as e:
            log.logger.error(f"Failed to get all search results count: {e}")
            raise

    def first_search_result_title(self):
        try:
            title_element = self.get_element(By.XPATH, configData.XPATH["first_Search_Result_Title"])
            title = title_element.text
            log.logger.info(f"First search result title: {title}")
            return title
        except Exception as e:
            log.logger.error(f"Failed to get first search result title: {e}")
            raise

    def first_search_result_address(self):
        try:
            address_element = self.get_element(By.XPATH, configData.XPATH["first_Search_Result_Address"])
            address = address_element.text
            self.click_element(By.XPATH, configData.XPATH["first_Search_Result_Address"])
            log.logger.info(f"First search result address: {address}")
            return address
        except Exception as e:
            log.logger.error(f"Failed to get first search result address: {e}")
            raise

    def search_center_name(self):
        try:
            time.sleep(5)
            center_element = self.get_element(By.XPATH, configData.XPATH["search_Center_Name"])
            center_name = center_element.text
            log.logger.info(f"Search center name: {center_name}")
            return center_name
        except Exception as e:
            log.logger.error(f"Failed to get search center name: {e}")
            raise

    def search_center_address(self):
        try:
            address_element = self.get_element(By.XPATH, configData.XPATH["search_Center_Address"])
            center_address = address_element.text.replace("\n", " ")
            log.logger.info(f"Search center address: {center_address}")
            return center_address
        except Exception as e:
            log.logger.error(f"Failed to get search center address: {e}")
            raise
