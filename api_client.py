import requests
import allure
import logging

logger = logging.getLogger(__name__)


class AvitoApiClient:
    def __init__(self):
        self.base_url = "https://qa-internship.avito.com"

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        logger.info(f"Request: {method} {url} | Payload: {kwargs.get('json')}")

        with allure.step(f"API Request: {method} {endpoint}"):
            response = requests.request(method, url, **kwargs)

            duration_ms = response.elapsed.total_seconds() * 1000
            logger.info(f"Response: {response.status_code} | Time: {duration_ms:.2f}ms")

            log_content = (
                f"Method: {method}\n"
                f"URL: {url}\n"
                f"Status: {response.status_code}\n"
                f"Response Time: {duration_ms:.2f}ms\n"
                f"Response Body: {response.text}"
            )
            allure.attach(
                log_content,
                name="Request-Response Details",
                attachment_type=allure.attachment_type.TEXT,
            )

            return response

    def create_item(self, payload):
        """Создать объявление"""
        return self._make_request("POST", "/api/1/item", json=payload)

    def get_item(self, item_id):
        """Получить объявление по его идентификатору"""
        return self._make_request("GET", f"/api/1/item/{item_id}")

    def get_seller_items(self, seller_id):
        """Получить все объявления по идентификатору продавца"""
        return self._make_request("GET", f"/api/1/{seller_id}/item")

    def get_stats(self, item_id):
        """Получить статистику по айтем id"""
        return self._make_request("GET", f"/api/1/statistic/{item_id}")

    def delete_item(self, item_id):
        """Удалить объявление (v2 из коллекции)"""
        return self._make_request("DELETE", f"/api/2/item/{item_id}")
