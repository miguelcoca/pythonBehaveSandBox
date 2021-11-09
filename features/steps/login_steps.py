from behave import *

@given('user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_gmail()

@when('user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then('the user is logged in')
def step_impl(context):
    context.inbox_page.logout()
