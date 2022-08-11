import allure
from selene.browser import open_url
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from framework.ui_pages.main_page import GmailMainPage


class GmailLoginPage:

    def __init__(self):
        self.login_field = s('input#identifierId')
        self.email_next_button = s('#identifierNext')
        self.password_field = s('div#password input')
        self.pass_next_button = s('#passwordNext')

    def open(self):
        open_url('/')
        return self

    @allure.step("Авторизоваться")
    def login(self, login, password):
        self.login_field.set(login)
        self.email_next_button.click()
        self.password_field.set(password)
        self.pass_next_button.click()
        main_page = GmailMainPage()
        main_page.create_message_button.should(be.existing)
        return main_page

