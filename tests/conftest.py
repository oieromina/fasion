import os
import pytest

BASE_URLS = {
    "prod": "https://automationexercise.com/"
}

@pytest.fixture(scope="session")
def base_url():
    env = os.getenv("ENV", "prod")
    return BASE_URLS[env]

@pytest.fixture(scope="session")
def user_name():
    return os.getenv("TEST_USER_NAME", "default_user")
@pytest.fixture(scope="session")
def user_email():
    return os.getenv("TEST_USER_EMAIL", "oieromina1@gmail.com")

@pytest.fixture(scope="session")
def password():
    return os.getenv("TEST_PASSWORD", "123456789")