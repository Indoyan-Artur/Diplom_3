import pytest
import requests
from selenium import webdriver
from uuid import uuid4

from page_objects import AuthorizationUserPage
from config import URL_AUTHORIZATION_PAGE, BASE_URL
from test_data import REGISTER_CASE


def get_webdriver(browser_name):
    if browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "chrome":
        return webdriver.Chrome()
    else:
        raise ValueError(f"Браузер '{browser_name}' не поддерживается")

@pytest.fixture(scope="class", params=["firefox", "chrome"])
def browser(request):
    driver = get_webdriver(request.param)
    yield driver
    driver.quit()

@pytest.fixture()
def registered_user():
    name = REGISTER_CASE["name"]
    email = f"test_{uuid4().hex[:8]}@example.com"
    password = REGISTER_CASE["password"]
    resp = requests.post(f"{BASE_URL}/api/auth/register",json={"name": name, "email": email, "password": password},)
    assert resp.status_code in (200, 201), f"Регистрация не удалась: {resp.status_code} {resp.text}"
    return name, email, password

@pytest.fixture()
def authorization_user(registered_user, browser):
    name, email, password = registered_user
    auth_page = AuthorizationUserPage(browser)
    auth_page.open_(URL_AUTHORIZATION_PAGE)
    auth_page.authorization_user(email, password)
    yield name, email, password

    from page_objects import PersonalAccountPage
    account = PersonalAccountPage(browser)
    if account.is_logged_in(timeout=1):
        account.exit()