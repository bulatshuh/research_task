import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url_api', default='https://playground.learnqa.ru/api_dev')
    parser.addoption('--url_web', default='https://vk.com')
    parser.addoption('--browser', default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        print('Opening Chrome...')
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('Opening Firefox...')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    yield browser
    print('Closing browser...')
    browser.quit()


@pytest.fixture(scope='session')
def get_url_web(request):
    url = request.config.getoption('url_web')
    yield url


@pytest.fixture(scope='session')
def get_url_api(request):
    url = request.config.getoption('url_api')
    yield url
