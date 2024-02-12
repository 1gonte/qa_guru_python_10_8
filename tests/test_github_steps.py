import allure
from allure_commons.types import Severity
from selene import browser, be, by


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "1gonte")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может просмотреть issues в репозитории")
@allure.link("https://github.com", name="Testing")
def test_should_be_issue_steps():
    with allure.step('Открываем главную страницу github.com'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('yashaka/selene').press_enter()

    with allure.step('Открываем репозиторий'):
        browser.element('[href="/yashaka/selene"]').click()

    with allure.step('Открываем вкладку issues'):
        browser.element('#issues-tab').click()

    with allure.step('Ищем номер нужной issue'):
        browser.element(by.partial_text('#513')).should(be.visible)
