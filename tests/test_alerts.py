import allure
from demoqa_tests.model.pages.alerts import AlertsPage

alerts = AlertsPage()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title('Подтверждение оповещения')
def test_confirm_alert():
    with allure.step('Открытие страницы оповещений'):
        alerts.open()
    with allure.step('Клик по кнопке для вызова оповещения'):
        alerts.click_btn_with_confirm()
    with allure.step('Проверка подтверждения оповещения'):
        alerts.assert_confirm_alert()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title('Подтверждение оповещения с заполнением текстового поля')
def test_prompt_alert():
    with allure.step('Открытие страницы оповещений'):
        alerts.open()
    with allure.step('Клик по кнопке для вызова оповещения'):
        alerts.click_btn_with_prompt()
    with allure.step('Ввод значения в текстовое поле в оповещении'):
        alerts.type_to_alert('asantalov')
    with allure.step('Проверка подтверждения оповещения'):
        alerts.assert_prompt_alert('asantalov')
