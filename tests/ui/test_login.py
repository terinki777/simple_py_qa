import allure
import pytest

from framework.resources.test_params.email_data import BaseEmail
from framework.resources.test_params.login_data import BaseLogin
from framework.ui_pages.login_page import GmailLoginPage


@pytest.mark.positive
@pytest.mark.usefixtures('allure_screen')
@allure.feature('Gmail.com Расылка писем')
class TestRegistrationForm:
    auth = BaseLogin
    email_data = BaseEmail

    @allure.story('Отправить письмо')
    @allure.testcase('https://gmail.com/', name='Ссылка на тест-кейс')
    @pytest.mark.parametrize('email', email_data.emails)
    @pytest.mark.usefixtures("close_driver_after_test")
    def test_send_email(self, email):
        """
        Описание теста.
        Открыть страницу https://gmail.com/
        """
        login_page = GmailLoginPage().open()
        main_page = login_page.login(login=self.auth.login, password=self.auth.password)
        main_page.create_and_send_message(email_to=email,
                                          email_subject=self.email_data.email_subject,
                                          email_text=self.email_data.email_text)
