import allure

# Проверить:
# Произошёл ли переход на главную страницу,
# отображается ли кнопка «Выход»

class TestAutorizationPage:

    @allure.title('Тест залогились, проверили переход на главную')
    def test_login_check_main(self, login_page):
        title = login_page.log_in_main()
        assert title == 'Рецепты'

    @allure.title('Тест залогинились, кнопка Выход отображается')
    def test_login_check_logout(self, login_page):
        title = login_page.log_in_and_text_logout()
        assert title == 'Выход'