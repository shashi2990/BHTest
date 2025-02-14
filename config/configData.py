
# please change broswer name here
BROWSER = "chrome"
PAGE_LOAD_TIMEOUT = 10
WAIT = 10
BASE_URL = "https://www.brighthorizons.com/"

XPATH = {
    "serach_Bar_On_CenterPage" : "//input[@id='addressInput']",
    "enter_Key_On_SearchBar" : "//input[@id='addressInput']",
    "final_Count" : "//span[@class='resultsNumber']",
    "get_All_Counts" : "//div[@class='centerResult infoWindow track_center_select covidOpen']",
    "first_Search_Result_Title" : "//h3[text()='Bright Horizons at TriBeCa']",
    "first_Search_Result_Address" : "//span[text()='129 Hudson Street  New York, NY 10013 ']",
    "search_Center_Name" : "//span[text()='Bright Horizons at TriBeCa']",
    "search_Center_Address" : "//div[@class='mapTooltip__address']",
    "close_Welcome_Banner" : "//button[text()='Accept All']",
    "search_Button" : "//a[@href='#subnav-search-desktop-top']//span[@class='icon-search bhc-icon-search-rounded']",
    "search_Bar" : "//nav[@id='subnav-search-desktop-top']//input[@id='search-field']",
    "search_By_Text" : "//nav[@id='subnav-search-desktop-top']//input[@id='search-field']",
    "search_Tab" : "//nav[@id='subnav-search-desktop-top']//button[@type='submit'][normalize-space()='Search']",
    "find_Center" : "(//li[@class='nav-item displayed-desktop']/a[normalize-space()='Find a Center'])[2]",
    "get_Text" : "//h3[normalize-space()='Employee Education in 2018: Strategies to Watch']"

}

TEST_DATA = {
    "city" : "New York",
    "search_Text" : "Employee Education in 2018: Strategies to Watch"
}

