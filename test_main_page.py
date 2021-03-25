# git init → git add . → git status → git commit -m "Adding a project" - запушить в git
# pytest -v --tb=line --language=en ~/PycharmProjects/SeleniumCourse/test_main_page.py - --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина