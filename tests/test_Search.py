import pytest
from tests.test_base import BaseTest
from pages.HomePage import HomePage
from config.config import Config


class TestSearch(BaseTest):
    def test_correct_page(self):
        self.HomePage = HomePage(self.driver)
        received_title = self.HomePage.get_home_page_title(Config.HOME_PAGE_TITLE)
        assert received_title == Config.HOME_PAGE_TITLE, "Некоректная страница"

    def test_search_field_exists(self):
        self.HomePage = HomePage(self.driver)
        search_field_exists_flag = self.HomePage.is_search_field_exist()
        assert search_field_exists_flag, "Нет поля ввода поискового запроса"

    def test_suggest_field_shown(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.fill_search_field(Config.SEARCH_TEXT)
        is_shown_flag = self.HomePage.is_suggest_table_shown()
        assert is_shown_flag, "Таблица с подсказками не появилась"

    def test_search_result_table_shown(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.fill_search_field(Config.SEARCH_TEXT)
        self.SearchPage = self.HomePage.do_search()
        is_search_result_table_shown_flag = self.SearchPage.is_search_result_table_exist()
        assert is_search_result_table_shown_flag, "Нет Результата поиска"

    def test_first_five_results_contain_link(self):
        self.HomePage = HomePage(self.driver)
        self.HomePage.fill_search_field(Config.SEARCH_TEXT)
        self.SearchPage = self.HomePage.do_search()
        assert self.SearchPage.is_search_result_table_exist(), "Нет Результата поиска"
        is_search_results_contain_link_flag = self.SearchPage.is_search_result_table_contain_link(Config.TENSOR_LINK, 5)
        assert is_search_results_contain_link_flag, f"Первые пять результатов не содержат {Config.TENSOR_LINK} ссылки"



