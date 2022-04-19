from tests.test_base import BaseTest
from pages.SearchPage import SearchPage
from config.config import Config


class TestImageSearch(BaseTest):
    def test_yandex_images_navigation(self):
        # Verify Icon
        self.SearchPage = SearchPage(self.driver)
        images_link_flag = self.SearchPage.is_images_link_exist()
        assert images_link_flag, "Icon with link to `yandex.ru/images` does NOT exist"

        # Go to Image Search
        self.ImageSearchPage = self.SearchPage.go_to_images_search_page()
        received_url = self.ImageSearchPage.get_url(Config.IMAGES_SEARCH_URL)
        assert Config.IMAGES_SEARCH_URL in received_url, "Navigation to `yandex.ru/images` was unsuccessful, URL is wrong"

        # Open first Category
        category_text = self.ImageSearchPage.get_first_category_text()
        self.ImageSearchPage.go_to_first_category()
        is_category_opened_flag = self.ImageSearchPage.is_title_with_search_text(category_text)
        assert is_category_opened_flag, "Opened Category is wrong, different Category was chosen"
        search_text = self.ImageSearchPage.get_search_field_text()
        assert search_text == category_text, "search line contains WRONG search text"

        # Image to Image Navigation
        self.ImageSearchPage.open_first_image()
        is_image_opened_flag = self.ImageSearchPage.is_image_opened()
        assert is_image_opened_flag, "Image wasn't opened"
        first_image_url = self.ImageSearchPage.get_image_url()
        self.ImageSearchPage.go_to_next_image()
        second_image_url = self.ImageSearchPage.get_image_url()
        assert first_image_url != second_image_url, "After switching image Image is the same"
        self.ImageSearchPage.go_to_previous_image()
        first_image_url_again = self.ImageSearchPage.get_image_url()
        assert first_image_url == first_image_url_again, "Image changed after going back to first image"
