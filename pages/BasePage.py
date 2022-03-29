from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

"""Base class for all Pages"""
"""Contains all generic methods and functionalities of all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.title_is(title))
        return self.driver.title

    def do_press_keys(self, by_locator, key):
        WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.visibility_of_element_located(by_locator)).send_keys(key)

    def get_title_with_text(self, text):
        WebDriverWait(self.driver, Config.TIME_WAIT).until(EC.title_contains(text))
        return self.driver.title

