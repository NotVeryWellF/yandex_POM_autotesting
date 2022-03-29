import pytest
from selenium import webdriver
from config.config import Config
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    service = Service(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(Config.TIME_WAIT)
    yield
    web_driver.quit()
