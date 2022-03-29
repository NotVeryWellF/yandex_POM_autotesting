from config.config import Config
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(BasePage):
    """Search page of the Yandex"""
    SEARCH_RESULT_TABLE = (By.ID, "search-result")
    RESULTS_IN_TABLE = (By.CLASS_NAME, "Link_theme_normal")

    def __init__(self, driver):
        super().__init__(driver)

    def is_title_with_search_text(self, text):
        title = self.get_title_with_text(text)
        return bool(title)

    def is_search_result_table_exist(self):
        return self.is_visible(self.SEARCH_RESULT_TABLE)

    def is_search_result_table_contain_link(self, link, number_of_results):
        search_results = WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.presence_of_all_elements_located(self.RESULTS_IN_TABLE))
        links = [elem.get_attribute('href') for elem in search_results]
        for i in range(min(len(links), number_of_results)):
            if link not in links[i]:
                return False
        return True

