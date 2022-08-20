import allure
from selene.support import by
from selene.support.jquery_style_selectors import s


class KinopoiskSearchResultPage:

    def __init__(self):
        self.search_results_element = s(
            by.xpath("//div[@class='search_results search_results_last']"))

    @allure.step("Результат поиска")
    def search_by_film_name(self):
        element_list = self.search_results_element
        return element_list.text