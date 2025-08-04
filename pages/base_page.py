import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# класс общих методов
class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('находим элемент после загрузки страницы')
    def find_element_with_wait(self, locator):
        (WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(locator)))
        return self.browser.find_element(*locator)

    @allure.step('клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        self.browser.find_element(*locator).click()

    @allure.step('ожидание пока не появится')
    def wait_element(self, locator):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('переходим по ссылке')
    def open_url(self, url):
        self.browser.get(url)

    @allure.step('скролл к элементу')
    def scroll_to_element(self, locator):
        (WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(locator)))
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('заполняем элемент данными')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

