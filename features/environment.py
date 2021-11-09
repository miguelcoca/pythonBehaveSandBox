from features.browser import Browser
from features.pages.login_page import LoginPage


def before_all(context):

    # user credentials
    username = 'redridehell@gmail.com'
    password = 'password'

    context.browser = Browser()
    context.login_page = LoginPage()

    context.login_page.navigate_to_gmail()
    context.login_page.login(username, password)


def after_all(context):
    context.browser.close()
