from selenium.webdriver.common.by import By


# локаторы страницы регистрации
class RegistrationLocators:

    # #кнопка войти в аккаунт
    # INACCOUNT = (By.XPATH, "//*[contains(@class, 'style_link__1kPh8 styles_menuButton') "
    #                        "and text()='Создать аккаунт']")
    #инпут для поля Имя
    INPUT_NAME = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                            "and text()='Имя']/following-sibling::input")
    #инпут для поля Фамилия
    INPUT_SURNAME = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                               "and text()='Фамилия']/following-sibling::input")
    #инпут для поля Имя пользователя
    INPUT_LOGIN = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                             "and text()='Имя пользователя']/following-sibling::input")
    #инпут для поля email
    INPUT_EMAIL = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                             "and text()='Адрес электронной почты']/following-sibling::input")
    #инпут для поля password
    INPUT_PASSWORD= (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                               "and text()='Пароль']/following-sibling::input")
    #кнопка Создать аккаунт
    BUTTON_CREATE_ACCOUNT = (By.XPATH, "//*[contains(@class,'style_button') "
                                       "and text()='Создать аккаунт']")
    #название панели Войти на сайт
    LABEL_LOGIN_TO_SITE = (By.XPATH, "//*[contains(@class, 'styles_title') "
                                     "and text() = 'Войти на сайт']")