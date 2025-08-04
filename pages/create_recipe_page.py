# Создание рецепта
# Авторизоваться и перейти на таб «Создать рецепт».
# Заполнить все поля формы создания рецепта и нажать кнопку «Создать рецепт».
# Примечание (ингредиент должен быть добавлен из списка, для отображения списка необходимо начать вводить название ингридиента в поле ввода)

import pyautogui
import allure
from pages.base_page import BasePage
from locators.create_recipe_locator import CreateRecipeLocators
from data import NAME_RECIPE, INGREDIENT, COOKING_TIME, RECIPE, GRAMS, ADDRESS_FOTO


# класс страницы регистрации
class CreateRecipePage(BasePage):
    @allure.step('Создаем аккаунт, возвращаем текст с Заголовка')
    def create_recipe(self):
        self.click_to_element(CreateRecipeLocators.TAB_CREATE_RECIPE)
        self.add_text_to_element(CreateRecipeLocators.INPUT_NAME_RECIPE, NAME_RECIPE)
        #добавление ингредиента
        self.add_text_to_element(CreateRecipeLocators.INPUT_INGREDIENT, INGREDIENT)
        self.click_to_element(CreateRecipeLocators.LIST_INGREDIENTS)
        self.wait_element(CreateRecipeLocators.INPUT_GRAMS)
        self.add_text_to_element(CreateRecipeLocators.INPUT_GRAMS, GRAMS)
        self.click_to_element(CreateRecipeLocators.BUTTON_ADD_INGREDIENT)
        self.wait_element(CreateRecipeLocators.INPUT_COOKING_TIME)
        self.add_text_to_element(CreateRecipeLocators.INPUT_COOKING_TIME, COOKING_TIME)
        self.scroll_to_element(CreateRecipeLocators.INPUT_RECIPE)
        self.add_text_to_element(CreateRecipeLocators.INPUT_RECIPE, RECIPE)
        #блок добавление фото, загрузка данных

        self.click_to_element(CreateRecipeLocators.BUTTON_ADD_FOTO)
        pyautogui.write(ADDRESS_FOTO)
        pyautogui.press('enter')
        self.click_to_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE)
        self.wait_element(CreateRecipeLocators.NAME_OUR_RECIPE)
        return self.get_text_from_element(CreateRecipeLocators.NAME_OUR_RECIPE)


