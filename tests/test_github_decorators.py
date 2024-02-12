from allure_commons.types import Severity

from utils.decorators import *


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "1gonte")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может просмотреть issues в репозитории")
@allure.link("https://github.com", name="Testing")
def test_should_be_issue_decorator():
    open_the_main_page()
    search_for_the_repository('yashaka/selene')
    open_the_repository('/yashaka/selene')
    open_the_issues_tab()
    search_for_the_issue('#513')
