from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import Config
from pages.ImageSearchPage import ImageSearchPage


class SearchPage(BasePage):
    """
    Search (Home) page of the Yandex
    https://yandex.ru
    """
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Config.BASE_URL)

    def is_images_link_exist(self):
        return self.is_visible(self.IMAGES_LINK)

    def go_to_images_search_page(self):
        url = self.get_element_attribute(self.IMAGES_LINK, 'href')
        self.go_to_url(url)
        return ImageSearchPage(self.driver)
