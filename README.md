## Проект UI автотестов для сайта demoqa.com
### Используемые технологии
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jira" src="https://logojinni.com/image/logos/jira-3.svg"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="Selenoid" src="https://diginomica.com/sites/default/files/images/2017-09/docker-container.jpg"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"></code>
</p>
<br> 

### Что проверяют тесты
* Подтверждение оповещения
* Подтверждение оповещения с заполнением текстового поля
* Открытие второй вкладки в браузере
* Успешная регистрация
* Успешная регистрация с обязательными полями
* Подсказка для текстового поля
<br>


### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/asantalov_diplom_ui/)
##### Реализована параметризованная сборка, для запуска проекта нужно выбрать браузер и его версию.
![Jenkins_run](/images/sborka.jpg)




### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете.
![Overview](images/allure.jpg)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги. UI тесты имеют вложения: скриншот, видео теста, лог и page_source.
![Behaviors](images/allure1.jpg)

##### Видео теста Подсказка для текстового поля.

https://user-images.githubusercontent.com/87572795/228360684-d7342cc6-eede-4396-9607-a5f5b9350266.mp4



### <img width="3%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"> [Интеграция с Allure TestOps](https://allure.autotests.cloud/project/2098/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![Graf](images/testop.jpg)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![tests](images/testops.jpg)


### <img width="3%" title="Jira" src="https://logojinni.com/image/logos/jira-3.svg"> [Интеграция с Jira](https://jira.autotests.cloud/browse/HOMEWORK-633)
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![Jira](images/Jira.jpg)


### <img width="3%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![Telegram](images/telega.jpg)








