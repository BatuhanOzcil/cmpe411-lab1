"""Lab 1, Task 4: a first end-to-end test with Playwright.

Run with:  pytest tests/test_todo_e2e.py --headed
"""
from playwright.sync_api import Page, expect

APP_URL = "https://demo.playwright.dev/todomvc/"


def test_add_one_todo(page: Page):
    page.goto(APP_URL)
    page.get_by_placeholder("What needs to be done?").fill("Buy milk")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_have_text(["Buy milk"])


# TODO (Task 4): write a test that adds two todos, marks the first one as
# completed and checks that "1 item left" is shown.
def test_complete_first_of_two_todos(page: Page):
    page.goto(APP_URL)

    todo_input = page.get_by_placeholder(
        "What needs to be done?"
    )

    todo_input.fill("Study for CMPE 411")
    todo_input.press("Enter")

    todo_input.fill("Finish the lab")
    todo_input.press("Enter")

    page.get_by_test_id("todo-item").nth(0).get_by_role(
        "checkbox"
    ).check()

    expect(
        page.get_by_test_id("todo-count")
    ).to_contain_text("1 item left")

