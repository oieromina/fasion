import os
import pytest

BASE_URLS = {
    "local": "http://localhost:4000/fashionhub",
    "staging": "https://staging-env/fashionhub",
    "prod": "https://pocketaces2.github.io/fashionhub"
}

@pytest.fixture(scope="session")
def base_url():
    env = os.getenv("ENV", "prod")
    return BASE_URLS[env]