from selene.support import by
from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from framework.utils import attach_allure_screen


class NewEmailBlock:

    def __init__(self):
        self.email_dialog = s('[role="dialog"]')
        self.email_to = s('[name="to"]')
        self.email_subject = s('[name="subjectbox"]')
        self.email_text = s('[role="textbox"]')
        self.email_send_button = s(by.xpath('//*[contains(@data-tooltip, "Enter")]'))

        self.email_sended_undo_link = s('#link_undo')
        self.email_sended_view_link = s('#link_vsm')


class GmailMainPage:

    def __init__(self):
        self.create_message_button = s('[gh="cm"]')
        self.alert_dialog = s('[role="alertdialog"]')

    def create_and_send_message(self, email_to, email_subject, email_text):
        self.create_message_button.click()

        new_email = NewEmailBlock()
        new_email.email_to.send_keys(email_to)
        new_email.email_subject.send_keys(email_subject)
        new_email.email_text.send_keys(email_text)
        attach_allure_screen(new_email.email_dialog, attach_name='Диалог "Новое сообщение"')
        new_email.email_send_button.click()

        new_email.email_sended_undo_link.should(be.visible)
        new_email.email_sended_view_link.should(be.visible)
