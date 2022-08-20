import time

import allure
import pytest
from framework.resources.test_params.search_data import BaseSearch
from framework.ui_pages.search_page import KinopoiskExtendedSearchPage
from framework.ui_pages.search_result_page import KinopoiskSearchResultPage


@pytest.mark.positive
@pytest.mark.usefixtures('allure_screen')
@allure.feature('Поиск фильма')
class TestSearch:
    bs = BaseSearch

    @allure.story('Поиск фильма')
    @allure.testcase('https://www.kinopoisk.ru/s/', name='Ссылка на тест-кейс')
    @pytest.mark.parametrize('film', bs.base_film)
    @pytest.mark.usefixtures("close_driver_after_test")
    def test_search(self, film):
        """
        Описание теста.
        Открыть страницу https://www.kinopoisk.ru/s/
        """
        film = film
        time.sleep(2)
        search_page = KinopoiskExtendedSearchPage().open()
        time.sleep(2)
        search_page.search_by_film_name(field_search=film)
        search_page.search_by_year(year=self.bs.base_year)
        search_page.film_genre(genre=self.bs.base_genre)
        search_page.film_country(country=self.bs.base_country)
        search_page.click_button_search()

    @allure.story('Результат поиска')
    @allure.testcase('https://www.kinopoisk.ru/s/', name='Ссылка на тест-кейс')
    @pytest.mark.usefixtures("close_driver_after_test")
    def test_result_search(self):
        """
        Описание теста.
        Открыть страницу https://www.kinopoisk.ru/s/
        """
        time.sleep(3)
        search_page = KinopoiskExtendedSearchPage().open()
        time.sleep(3)
        search_page.search_by_year(year=self.bs.base_year)
        search_page.film_genre(genre=self.bs.base_genre)
        search_page.film_country(country=self.bs.base_country)
        search_page.click_button_search()
        result_page = KinopoiskSearchResultPage()

        assert "Унесённые призраками" in result_page.search_by_film_name()
