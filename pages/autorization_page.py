# Авторизация
# Нажать кнопку «Войти».
# Заполнить все поля формы авторизации и нажать кнопку «Войти».

import helpers
import allure
from pages.base_page import BasePage
from locators.autorization_locator import AutorizationLocators
from data import EMAIL, PASSWORD

# класс страницы регистрации
class AutorizationPage(BasePage):

    @allure.step('Создаем аккаунт, возвращаем текст с Заголовка')
    def log_in_main(self):
        self.click_to_element(AutorizationLocators.BUTTON_LOGIN_MAIN)

        self.add_text_to_element(AutorizationLocators.INPUT_EMAIL, EMAIL)
        self.add_text_to_element(AutorizationLocators.INPUT_PASSWORD, PASSWORD)

        self.click_to_element(AutorizationLocators.BUTTON_LOGIN)
        return self.get_text_from_element(AutorizationLocators.PANEL_RECIPE)

    def log_in_and_text_logout(self):
        self.click_to_element(AutorizationLocators.BUTTON_LOGIN_MAIN)

        self.add_text_to_element(AutorizationLocators.INPUT_EMAIL, EMAIL)
        self.add_text_to_element(AutorizationLocators.INPUT_PASSWORD, PASSWORD)

        self.click_to_element(AutorizationLocators.BUTTON_LOGIN)
        return self.get_text_from_element(AutorizationLocators.BUTTON_LOGOUT)