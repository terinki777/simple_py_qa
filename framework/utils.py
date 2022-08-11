import allure
import selene
from selene import factory
from allure_commons.types import AttachmentType

from framework.config import FrameworkConfig


def screen_for_allure():
    attach_allure_screen(attach_name='screen_after_step')


def screen_for_allure_on_fail():
    attach_allure_screen(attach_name='screen_on_fail')


def attach_allure_screen(element=None, attach_name='screen'):
    if not FrameworkConfig().use_allure:
        return

    try:
        if element is None:
            screen = selene.factory.get_shared_driver().get_screenshot_as_png()
        else:
            screen = element.screenshot_as_png

        allure.attach(screen, name=attach_name, attachment_type=AttachmentType.PNG)
    except Exception as err:
        print(f'Error on attach allure screen: {err}')
