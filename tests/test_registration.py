import allure

# Проверить:
# Произошёл ли переход на страницу авторизации,
# отображается ли форма авторизации.
class TestRegistrationPage:

    @allure.title('Тест а создание аккаунта')
    @allure.description('Переходим на страницу создание пользователя, заполняем все поля и нажимаем Создать')
    def test_window_with_details(self, registration_page):
        title = registration_page.create_account()
        assert title == 'Войти на сайт'

