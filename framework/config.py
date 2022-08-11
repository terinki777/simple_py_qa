import os
from configparser import ConfigParser

import selene
from selene import config

from framework.resources.test_params.email_data import BaseEmail


class FrameworkConfig:
    __instance = None

    def __new__(cls, pytest_config=None):
        if cls.__instance is None:
            if pytest_config is None:
                raise TypeError("Empty pytest_config param")
            cls.__instance = FrameworkConfigInstance(pytest_config)
        return cls.__instance


class FrameworkConfigInstance:

    def __init__(self, pytest_config):
        self.pytest_config = pytest_config
        self.root_path = pytest_config.rootdir.strpath
        self.config_file = f'{self.root_path}/defaults.ini'
        self.use_allure = False

        self.config_reader = ConfigParser()
        self.config_reader.read(self.config_file)
        self.configure_selenium()
        self.configure_selene()
        self.configure_allure()
        self.configure_test_data()

    def configure_selenium(self):
        section = 'selenium'
        self.pytest_config.option.browser = self.get_value(section, 'browser', conf_default='chrome')
        self.pytest_config.option.windows_size = self.get_value(section, 'windows_size')
        self.pytest_config.option.driver_url = self.get_value(section, 'driver_url')
        self.pytest_config.option.browser_version = self.get_value(section, 'browser_version')

    def configure_selene(self):
        section = 'selene'
        selene.config.base_url = self.get_value(section, 'base_url', conf_default='https://gmail.com/')
        selene.config.timeout = int(self.get_value(section, 'timeout', conf_default=10))
        selene.config.poll_during_waits = float(self.get_value(section, 'poll_during_waits', conf_default=0.5))
        reports_folder = self.get_value(section, 'reports_folder', conf_default='reports/selene/')
        if not os.path.isabs(reports_folder):
            reports_folder = f'{self.root_path}/{reports_folder}'
        selene.config.reports_folder = reports_folder

    def configure_allure(self):
        section = 'allure'
        allure_dir = self.get_value(section, 'alluredir', pytest_option_name='allure_report_dir')
        if allure_dir is not None:
            self.use_allure = True
            self.pytest_config.option.clean_alluredir = self.get_value(section, 'clean-alluredir',
                                                                       pytest_option_name='clean_alluredir')
            if not os.path.isabs(allure_dir):
                allure_dir = f'{self.root_path}/{allure_dir}'
            self.pytest_config.option.allure_report_dir = allure_dir
            self.pytest_config.option.clean_alluredir = True

    def configure_test_data(self):
        emails = getattr(self.pytest_config.option, 'emails', None)
        if emails is not None:
            BaseEmail.emails = emails.split(';')

    def get_value(self, conf_section, conf_var, conf_default=None, pytest_option_name=None):
        if pytest_option_name is None:
            pytest_option_name = conf_var
        pytest_option_value = getattr(self.pytest_config.option, pytest_option_name, None)
        if pytest_option_value is not None:
            return pytest_option_value
        return self.config_reader.get(conf_section, conf_var, fallback=conf_default)

    @staticmethod
    def get_resources_path():
        return f'{FrameworkConfig().root_path}/framework/resources/'

