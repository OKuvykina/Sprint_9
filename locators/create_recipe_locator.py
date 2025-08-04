from selenium.webdriver.common.by import By


# локаторы страницы авторизации
class CreateRecipeLocators:

    #вкладка Создать рецепт
    TAB_CREATE_RECIPE = (By.XPATH, "//*[contains(@class, 'style_link') "
                           "and text()='Создать рецепт']")

    #инпут для поля Название рецепта
    INPUT_NAME_RECIPE = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                            "and text()='Название рецепта']/following-sibling::input")

    #инпут для поля Ингредиенты
    INPUT_INGREDIENT = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                            "and text()='Ингредиенты']/following-sibling::input")

    #выпадающий список с ингредиентами Буррата
    LIST_INGREDIENTS = (By.XPATH, "//*[contains(@class, 'styles_container')]/div[text()='Буррата']")

    #инпут для количества граммов
    INPUT_GRAMS = (By.XPATH, "//*[contains(@class, 'styles_inputLabel')]/"
                             "input[contains(@class, 'styles_inputField__3eqTj styles_ingredientsAmountValue')]")
    #кнопка добавления ингредиента
    BUTTON_ADD_INGREDIENT = (By.XPATH, "//*[contains(@class,'styles_ingredientAdd') "
                            "and text()='Добавить ингредиент']")

    #инпут для поля Время приготовления
    INPUT_COOKING_TIME = (By.XPATH, "//*[contains(@class,'styles_inputLabelText') "
                            "and text()='Время приготовления']/following-sibling::input")
    #инпут для поля Описание рецепта
    INPUT_RECIPE = (By.XPATH, "//*[contains(@class,'styles_textareaLabelText') "
                            "and text()='Описание рецепта']/following-sibling::textarea")

    #кнопка добавления картинки
    BUTTON_ADD_FOTO = (By.XPATH, "//*[contains(@class,'styles_button') and text()='Выбрать файл']")

    BUTTON_INPUT_FOTO = (By.XPATH, "//*[contains(@class,'styles_label') "
                            "and text()='Загрузить фото']/following-sibling::input")

    BUTTON_CREATE_RECIPE = (By.XPATH, "//*[contains(@class, 'style_button') "
                           "and text()='Создать рецепт']")

    NAME_OUR_RECIPE = (By.XPATH, "//*[contains(@class, 'styles_single-card__header-info')]")


