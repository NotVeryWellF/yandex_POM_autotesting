from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ImageSearchPage(BasePage):
    """Image Search Page of the Yandex"""
    FIRST_CATEGORY = (By.CLASS_NAME, 'PopularRequestList-Item_pos_0')
    SEARCH_FIELD = (By.CLASS_NAME, 'mini-suggest__input')
    FIRST_IMAGE = (By.CLASS_NAME, 'serp-item_pos_0')
    OPENED_IMAGE_CONTAINER = (By.CLASS_NAME, 'MediaViewer-LayoutContainer')
    BUTTON_RIGHT = (By.CLASS_NAME, 'MediaViewer-ButtonNext')
    BUTTON_LEFT = (By.CLASS_NAME, 'MediaViewer-ButtonPrev')
    IMAGE = (By.CLASS_NAME, 'MMImage-Preview')

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_category_text(self):
        return self.get_element_attribute(self.FIRST_CATEGORY, "data-grid-text")

    def go_to_first_category(self):
        self.do_click(self.FIRST_CATEGORY)

    def is_title_with_search_text(self, text):
        title = self.get_title_with_text(text)
        return bool(title)

    def get_search_field_text(self):
        return self.get_element_attribute(self.SEARCH_FIELD, 'value')

    def open_first_image(self):
        self.do_click(self.FIRST_IMAGE)

    def is_image_opened(self):
        return self.is_visible(self.OPENED_IMAGE_CONTAINER)

    def get_image_url(self):
        return self.get_element_attribute(self.IMAGE, 'src')

    def go_to_next_image(self):
        self.do_click(self.BUTTON_RIGHT)

    def go_to_previous_image(self):
        self.do_click(self.BUTTON_LEFT)
