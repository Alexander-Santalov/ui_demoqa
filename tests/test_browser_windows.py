import allure
from demoqa_tests.model.pages.browser_windows import WindowPage

browser_windows = WindowPage()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title("Открытие второй вкладки в браузере")
def test_confirm_alert():
    with allure.step('Открытие страницы окна браузера'):
        browser_windows.open()
    with allure.step('Открытие второй вкладки'):
        browser_windows.click_btn_new_tab()
    with allure.step('Проверка текста на открытой вкладке'):
        browser_windows.assert_open_new_tab()
