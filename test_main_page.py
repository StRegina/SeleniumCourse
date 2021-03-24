# git init → git add . → git status → git commit -m "Adding a project" - запушить в git
# pytest -v --tb=line --language=en ~/PycharmProjects/SeleniumCourse/test_main_page.py - --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()