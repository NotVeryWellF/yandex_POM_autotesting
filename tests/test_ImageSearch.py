import pytest
from tests.test_base import BaseTest
from pages.HomePage import HomePage
from pages.ImageSearchPage import ImageSearchPage
from config.config import Config


class TestImageSearch(BaseTest):
    def test_is_images_link_exists(self):
        self.HomePage = HomePage(self.driver)
        images_link_flag = self.HomePage.is_images_link_exist()
        assert images_link_flag, "Ссылка «Картинки» отсутствует на странице"

    def test_go_to_images_search_page(self):
        self.HomePage = HomePage(self.driver)
        assert self.HomePage.is_images_link_exist(), "Ссылка «Картинки» отсутствует на странице"
        self.ImageSearchPage = self.HomePage.go_to_images_search_page()
        received_url = self.ImageSearchPage.get_url(Config.IMAGES_SEARCH_URL)
        assert Config.IMAGES_SEARCH_URL in received_url, "URL Яндекс Картинок не совпадает с текущем URL"

    def test_first_image_search_category(self):
        self.HomePage = HomePage(self.driver)
        self.ImageSearchPage = self.HomePage.go_to_images_search_page()
        category_text = self.ImageSearchPage.get_first_category_text()
        self.ImageSearchPage.go_to_first_category()
        is_category_opened_flag = self.ImageSearchPage.is_title_with_search_text(category_text)
        assert is_category_opened_flag, "Открытая категория не совпадает с выбранной"
        search_text = self.ImageSearchPage.get_search_field_text()
        assert search_text == category_text, "Поле поиска не совпадает с выбранной категорией"

    def test_work_with_images(self):
        self.HomePage = HomePage(self.driver)
        self.ImageSearchPage = self.HomePage.go_to_images_search_page()
        self.ImageSearchPage.go_to_first_category()
        self.ImageSearchPage.open_first_image()
        is_image_opened_flag = self.ImageSearchPage.is_image_opened()
        assert is_image_opened_flag, "Картинка не открылась"
        first_image_url = self.ImageSearchPage.get_image_url()
        self.ImageSearchPage.go_to_next_image()
        second_image_url = self.ImageSearchPage.get_image_url()
        assert first_image_url != second_image_url, "Картинка не поменялась"
        self.ImageSearchPage.go_to_previous_image()
        first_image_url_again = self.ImageSearchPage.get_image_url()
        assert first_image_url == first_image_url_again, "Картинка поменялась при переходе назад"



