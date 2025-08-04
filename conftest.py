import pytest
from selenium import webdriver
from data import URL_RECIPES, URL_LK_PAGES, URL_SIGNIN_PAGES, EMAIL, PASSWORD
from pages.registration_page import RegistrationPage
from pages.autorization_page import AutorizationPage
from pages.create_recipe_page import CreateRecipePage
from locators.autorization_locator import AutorizationLocators


@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture #заходим на страницу сайта для регистрации
def registration_page(browser):
    page = RegistrationPage(browser)
    page.open_url(URL_LK_PAGES)
    return page

@pytest.fixture #заходим на страницу сайта для авторизации
def login_page(browser):
    page = AutorizationPage(browser)
    page.open_url(URL_SIGNIN_PAGES)
    return page

@pytest.fixture #заходим на главную страницу сайта
def create_recipe_page(browser):
    page = CreateRecipePage(browser)
    page.open_url(URL_RECIPES)
    return page

#логинимся
@pytest.fixture
def login(login_page):

    login_page.click_to_element(AutorizationLocators.BUTTON_LOGIN_MAIN)
    login_page.add_text_to_element(AutorizationLocators.INPUT_EMAIL, EMAIL)
    login_page.add_text_to_element(AutorizationLocators.INPUT_PASSWORD, PASSWORD)

    login_page.click_to_element(AutorizationLocators.BUTTON_LOGIN)
    return login_page

