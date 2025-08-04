import allure
from data import NAME_RECIPE

# Проверить, отображается ли:
# карточка созданного рецепта,
# название, которое заполняли при создании.

class TestCreateRecipePage:

    @allure.title('Тест залогились, проверили переход на главную')
    def test_login_check_main(self, create_recipe_page, login):
        title = create_recipe_page.create_recipe()
        assert title == NAME_RECIPE

