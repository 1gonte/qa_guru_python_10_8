import allure
from allure_commons.types import Severity
from selene import browser, be, by


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "1gonte")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может просмотреть issues в репозитории")
@allure.link("https://github.com", name="Testing")
def test_should_be_issue():
    browser.open('/')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('yashaka/selene').press_enter()

    browser.element('[href="/yashaka/selene"]').click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#513')).should(be.visible)
