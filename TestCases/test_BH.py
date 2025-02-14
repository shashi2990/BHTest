import logging
import pytest

from config.configData import BASE_URL
from Pages.home_page import HomePage
from Pages.search_page import SearchPage
from Pages.findCenter_page import FindCenterPage
from driver.driverFactory import DriverFactory
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)
base_url = BASE_URL

@pytest.fixture(scope="function")
def setup():
    """Fixture to set up WebDriver before each test and close it after execution."""
    driver = DriverFactory.get_driver()
    driver.get(base_url)
    yield driver
    driver.quit()

def test_search_functionality(setup):
    driver = setup
    home_page = HomePage(driver)

    # Perform search
    home_page.close_welcome_banner()
    home_page.search_button()
    home_page.search_bar()
    home_page.search_by_text()
    home_page.search_tab()

    # Verify search result
    search_page = SearchPage(driver)
    result_text = search_page.get_text()
    expected_text = "Employee Education in 2018: Strategies to Watch"
    assert result_text == expected_text, f"Expected: '{expected_text}', but got: '{result_text}'"
    log.logger.info("Search functionality test passed!")

def test_find_center_functionality(setup):
    driver = setup
    home_page = HomePage(driver)

    # Navigate to Find Center
    home_page.close_welcome_banner()
    home_page.find_center()

    web_url = driver.current_url
    param_url = "child-care-locator"
    if param_url in web_url:
        print("Parameter is correctly applied in the URL")
    else:
        print("Parameter is missing or incorrect")
    log.logger.info("URL parameter is correctly applied.")

    # Search for centers
    find_center_page = FindCenterPage(driver)
    find_center_page.search_bar_on_centerpage()
    find_center_page.enter_key_on_searchBar()

    # Validate search results count
    find_center_page.final_count()
    total_count = find_center_page.final_count()
    find_center_page.get_all_counts()
    listed_count = find_center_page.get_all_counts()
    log.logger.info(f" Debug: total_count = '{total_count}', listed_count = '{listed_count}'")

    assert int(total_count) == int(listed_count), f"Count mismatch: Expected {total_count}, is with actual {listed_count}"

    first_title = find_center_page.first_search_result_title()
    first_address = find_center_page.first_search_result_address()
    center_name = find_center_page.search_center_name()
    center_address = find_center_page.search_center_address()

    assert first_title == center_name, f" Title mismatch: '{first_title}' vs '{center_name}'"
    assert first_address == center_address, f" Address mismatch: '{first_address}' vs '{center_address}'"
    log.logger.info("Center details matched. Test passed!")
