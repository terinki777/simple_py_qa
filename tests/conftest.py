from framework.config import FrameworkConfig


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', help='Base url')
    parser.addoption('--browser', action='store', help='Browser name. Default: chrome')
    parser.addoption('--windows_size', action='store', help='Window size. Default: full screen')
    parser.addoption('--driver_url', action='store', help='Selenoid/selenium grid url')
    parser.addoption('--browser_version', action='store', help='Browser version. Use in selenoid/selenium grid')
    parser.addoption('--emails', action='store', help='Email`s for send message (; as separator).')


def pytest_configure(config):
    FrameworkConfig(config)
