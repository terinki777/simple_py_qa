import allure
from selene.browser import open_url
from selene.support import by
from selene.support.jquery_style_selectors import s
from selenium.webdriver.support.ui import Select


class KinopoiskExtendedSearchPage:

    def __init__(self):
        self.field_search_film = s(by.xpath("//form[@class='form_1 js-rum-hero']/input[@class='text el_1']"))
        self.field_year = s(by.xpath("//form[@class='form_1 js-rum-hero']/input[@class='text el_2 __yearSB__']"))
        self.country_drop_down = s(by.xpath("//form[@class='form_1 js-rum-hero']"
                                            "/select[@class='text el_5 __countrySB__']"))
        self.button_search = s(by.xpath("//form[@class='form_1 js-rum-hero']/input[@type='button']"))
        self.choose_genre = s(by.xpath("//form[@class='form_1 js-rum-hero']/select[@class='text el_6 __genreSB__']"))
        self.choose_country = s(
            by.xpath("//form[@class='form_1 js-rum-hero']/select[@class='text el_5 __countrySB__']"))

    def open(self):
        open_url('/')
        return self

    @allure.step("Ввод фильма в поле 'Искать фильм'")
    def search_by_film_name(self, field_search):
        self.field_search_film.set(field_search)

    @allure.step("Ввод в поле '+год:'")
    def search_by_year(self, year):
        self.field_year.set(year)

    @allure.step("Нажать кнопку 'поиск'")
    def click_button_search(self):
        self.button_search.click()

    @allure.step("Выбрать жанр фильма")
    def film_genre(self, genre):
        select_genre = Select(self.choose_genre)
        select_genre.select_by_visible_text(genre)

    @allure.step("Выбрать страну")
    def film_country(self, country):
        select_country = Select(self.choose_country)
        select_country.select_by_visible_text(country)
