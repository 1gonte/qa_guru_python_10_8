import allure
from selene import browser, be, by


@allure.step('Открываем главную страницу')
def open_the_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий {repo}')
def search_for_the_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Открываем репозиторий {repo}')
def open_the_repository(repo):
    browser.element(f'[href="{repo}"]').click()


@allure.step('Открываем вкладку issues')
def open_the_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Ищем issue с номером {number}')
def search_for_the_issue(number):
    browser.element(by.partial_text(number)).should(be.visible)
