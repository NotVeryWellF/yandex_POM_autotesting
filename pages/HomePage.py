from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.config import Config
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    """Home page of the Yandex"""
    SEARCH_FIELD = (By.ID, "text")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup-content")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_search_field_exist(self):
        return self.is_visible(self.SEARCH_FIELD)

    def do_search(self):
        self.do_press_keys(self.SEARCH_FIELD, Keys.ENTER)
        return SearchPage(self.driver)

    def fill_search_field(self, text):
        self.do_send_keys(self.SEARCH_FIELD, text)

    def is_suggest_table_shown(self):
        return self.is_visible(self.SUGGEST_TABLE)
