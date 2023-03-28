import allure
from demoqa_tests.model.pages.tooltips import TooltipPage

tooltips = TooltipPage()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title('Подсказка для текстового поля')
def test_confirm_alert():
    with allure.step('Открытие страницы подсказки'):
        tooltips.open()
    with allure.step('Установка фокуса на поле'):
        tooltips.set_focus_in_field()
    with allure.step('Проверка текста подсказки'):
        tooltips.assert_text()
