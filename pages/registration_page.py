# Создание аккаунта
# Нажать кнопку «Создать аккаунт».
# Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».


import helpers
import allure
from pages.base_page import BasePage
from locators.registration_locator import RegistrationLocators
from data import EMAIL, PASSWORD

# класс страницы регистрации
class RegistrationPage(BasePage):

    @allure.step('Создаем аккаунт')
    def create_account(self):
        Name = helpers.register_new_string()
        self.add_text_to_element(RegistrationLocators.INPUT_NAME, Name)
        SurName = helpers.register_new_string()
        self.add_text_to_element(RegistrationLocators.INPUT_SURNAME, SurName)
        Login = helpers.register_new_string()
        self.add_text_to_element(RegistrationLocators.INPUT_LOGIN, Login)
        self.add_text_to_element(RegistrationLocators.INPUT_EMAIL, EMAIL)
        self.add_text_to_element(RegistrationLocators.INPUT_PASSWORD, PASSWORD)
        self.click_to_element(RegistrationLocators.BUTTON_CREATE_ACCOUNT)
        return self.get_text_from_element(RegistrationLocators.LABEL_LOGIN_TO_SITE)