import os
import sys

import selene
from selene import factory
from selenium import webdriver


class Platform:
    Windows = 'WINDOWS'
    Linux = 'LINUX'
    MacOS = 'MAC'


class BrowserName:
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    IE = 'explorer'


def get_platform_name():
    if 'linux' in sys.platform:
        return Platform.Linux
    if 'darwin' in sys.platform:
        return Platform.MacOS
    return Platform.Windows


def get_driver_path(browser_name):
    driver_exec = 'chromedriver'
    if browser_name == BrowserName.FIREFOX:
        driver_exec = 'geckodriver'
    if browser_name == BrowserName.IE:
        driver_exec = 'IEDriverServer'

    platform = get_platform_name()
    if platform == Platform.Windows:
        driver_exec = driver_exec + '.exe'

    framework_dir = os.path.dirname(os.path.abspath(__file__))
    return f'{framework_dir}/drivers/{platform}/{driver_exec}'


def get_chrome_capabilities():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    desired_capabilities['browserName'] = 'chrome'
    desired_capabilities['browser'] = 'Chrome'
    return desired_capabilities


def get_firefox_capabilities():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    desired_capabilities['browserName'] = 'firefox'
    desired_capabilities['browser'] = 'Firefox'
    return desired_capabilities


def get_ie_capabilities():
    desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
    desired_capabilities['ignoreProtectedModeSettings'] = True
    desired_capabilities['browserName'] = 'internet explorer'
    desired_capabilities['browser'] = 'IE'
    return desired_capabilities


def get_driver(driver_url, browser_name, browser_version):

    if browser_name == BrowserName.FIREFOX:
        caps = get_firefox_capabilities()
        local_driver_initializer = webdriver.Firefox
    elif browser_name == BrowserName.IE:
        caps = get_ie_capabilities()
        local_driver_initializer = webdriver.Ie
    else:
        caps = get_chrome_capabilities()
        local_driver_initializer = webdriver.Chrome

    if driver_url is None:
        return local_driver_initializer(executable_path=get_driver_path(browser_name), desired_capabilities=caps)
    else:
        if browser_version is not None:
            caps['browser_version'] = browser_version
            caps['version'] = browser_version

        return webdriver.Remote(command_executor=driver_url, desired_capabilities=caps)


def init_driver(pytest_config):
    browser_name = pytest_config.option.browser
    windows_size = pytest_config.option.windows_size
    driver_url = pytest_config.option.driver_url
    browser_version = pytest_config.option.browser_version

    driver = get_driver(driver_url, browser_name, browser_version)

    if windows_size is None:
        driver.maximize_window()
    else:
        driver.set_window_size(windows_size.split('x')[0], windows_size.split('x')[1])
    selene.factory.set_shared_driver(driver)


def close_driver():
    shared_driver = selene.factory.get_shared_driver()
    if selene.factory.is_driver_still_open(shared_driver):
        shared_driver.quit()


def init_driver_if_not_open(pytest_config):
    if not selene.factory.is_driver_still_open(selene.factory.get_shared_driver()):
        init_driver(pytest_config)


def init_new_driver(pytest_config):
    close_driver()
    init_driver(pytest_config)

