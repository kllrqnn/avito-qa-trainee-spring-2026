import pytest
import allure
import logging
from helpers import assert_status_code, get_id_from_response

logger = logging.getLogger(__name__)

@allure.feature("Объявления")
@allure.story("E2E Сценарий: Жизненный цикл объявления")
def test_item_lifecycle_e2e(api, item_payload):
    """
    Кейс E2E-1: Создание -> Получение по ID -> Проверка
    """
    with allure.step("Создать объявление через POST"):
        response = api.create_item(item_payload)
        assert_status_code(response, 200)
        
        item_id = get_id_from_response(response)
        assert item_id is not None, f"Не удалось извлечь ID из ответа: {response.text}"
        logger.info(f"Создано объявление с ID: {item_id}")

    with allure.step(f"Получить объявление по ID {item_id}"):
        response = api.get_item(item_id)
        assert_status_code(response, 200)
        
        item_data = response.json()[0]
        assert item_data["name"] == item_payload["name"]
        assert item_data["price"] == item_payload["price"]

    with allure.step(f"Проверить наличие объявления в списке продавца {item_payload['sellerId']}"):
        response = api.get_seller_items(item_payload["sellerId"])
        assert_status_code(response, 200)
        
        ids = [item["id"] for item in response.json()]
        assert item_id in ids, "Объявление не найдено в списке продавца"


@allure.feature("Объявления")
@allure.story("Нефункциональные проверки")
def test_get_item_performance(api, item_payload):
    """
    Кейс PERF-1: Проверка времени ответа
    """
    create_res = api.create_item(item_payload)
    item_id = get_id_from_response(create_res)
        
    with allure.step("Замерить время выполнения GET запроса"):
        response = api.get_item(item_id)
        assert_status_code(response, 200)
        
        duration_ms = response.elapsed.total_seconds() * 1000
        assert duration_ms < 500, f"Response time too slow: {duration_ms:.2f}ms"


@allure.feature("Объявления")
@allure.story("Корнер-кейсы")
def test_get_item_idempotency(api, item_payload):
    """
    Кейс IDM-1: Идемпотентность GET запроса
    """
    create_res = api.create_item(item_payload)
    item_id = get_id_from_response(create_res)

    with allure.step("Выполнить 3 одинаковых запроса"):
        responses = [api.get_item(item_id) for _ in range(3)]

    with allure.step("Проверить, что все ответы идентичны"):
        first_body = responses[0].json()
        for res in responses:
            assert_status_code(res, 200)
            assert res.json() == first_body, "Ответы различаются, GET не идемпотентен"


@allure.feature("Объявления")
@allure.story("Негативные сценарии")
@pytest.mark.parametrize("invalid_price", ["free", -100, None])
def test_create_item_invalid_price(api, item_payload, invalid_price):
    """
    Кейс CN-1, CN-2: Валидация некорректной цены
    """
    item_payload["price"] = invalid_price
    response = api.create_item(item_payload)

    with allure.step(f"Проверить, что цена {invalid_price} возвращает ошибку 400"):
        assert_status_code(response, 400)