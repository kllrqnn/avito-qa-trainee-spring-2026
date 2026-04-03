import pytest
import random
import logging
from api_client import AvitoApiClient


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )


@pytest.fixture(scope="session")
def api():
    """Доступ к API клиенту"""
    return AvitoApiClient()


@pytest.fixture
def item_payload():
    """Генератор случайных данных для объявления"""
    seller_id = random.randint(111111, 999999)
    return {
        "name": f"Test Gadget {random.randint(100, 999)}",
        "price": random.randint(1000, 50000),
        "sellerId": seller_id,
        "statistics": {
            "contacts": random.randint(0, 50),
            "likes": random.randint(0, 100),
            "viewCount": random.randint(0, 1000),
        },
    }
