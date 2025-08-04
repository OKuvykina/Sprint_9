from selenium.webdriver.common.by import By


# локаторы страницы авторизации
class AutorizationLocators:
    #кнопка Войти на главной странице
    BUTTON_LOGIN_MAIN = (By.XPATH, "//*[contains(@class, 'style_link') "
                           "and text()='Войти']")

    #инпут для поля email
    INPUT_EMAIL = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                            "and text()='Электронная почта']/following-sibling::input")
    #инпут для поля password
    INPUT_PASSWORD= (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                               "and text()='Пароль']/following-sibling::input")
    #панель Рецепты
    PANEL_RECIPE = (By.XPATH, "//*[contains(@class, 'styles_title') "
                           "and text()='Рецепты']")
    #кнопка войти в аккаунт
    BUTTON_LOGIN = (By.XPATH, "//*[contains(@class, 'style_button') "
                           "and text()='Войти']")
    #кнопка Выход
    BUTTON_LOGOUT = (By.XPATH, "//*[contains(@class, 'styles_menuLink') "
                              "and text()='Выход']")



