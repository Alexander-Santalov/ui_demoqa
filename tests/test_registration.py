from datetime import date
import allure

from demoqa_tests.model.pages import practice_form_module
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.model.data.student import Student, Hobby
from demoqa_tests.utils.parser_files import read_txt_file

practice_form = PracticePage()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title('Успешная регистрация')
def test_registration():
    student = Student(
        first_name='Alexander',
        last_name='Santalov',
        email='asantalov@bolid.ru',
        phone='8916777665',
        address='Zelenograd',
        birthday=date(1986, 8, 3),
        gender='Male',
        subject='Chemistry',
        hobby=[Hobby.Music, Hobby.Sports],
        image='Toolsqa.jpg',
        state='Haryana',
        city='Panipat')
    with allure.step('Открытие страницы регистрации'):
        practice_form.open()
    with allure.step('Заполнение формы'):
        practice_form.fill(student).submit()
    with allure.step('Проверка значений результирующей формы'):
        practice_form.assert_results_registration(student)


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты DemoQA')
@allure.title('Успешная регистрация с обязательными полями')
def test_registration_required_field():
    with allure.step('Открытие страницы регистрации'):
        practice_form_module.opening()
    with allure.step('Заполнение формы'):
        practice_form_module.fill_registration_form(*read_txt_file('student.txt'))
    with allure.step('Проверка значений результирующей формы'):
        practice_form_module.assert_results_registration(
            [('Student Name', 'Alexander Santalov'),
             ('Gender', 'Male'),
             ('Mobile', '8916777665')])
