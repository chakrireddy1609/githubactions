import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.utils import ChromeType


@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    chrome_options = Options()
    options = ["--headless", "--ignore-certificate-errors"]
    for option in options:
        chrome_options.add_argument(option)
    request.cls.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub',options = chrome_options)
    yield request.cls.driver
    request.cls.driver.close()
