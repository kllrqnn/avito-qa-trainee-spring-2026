import logging
import allure

logger = logging.getLogger(__name__)

def assert_status_code(response, expected_status=200):
    """
    Универсальная проверка статус-кода с логирование и Allure-отчетом
    """
    actual_status = response.status_code
    
    if actual_status != expected_status:
        error_msg = (
            f"\n ASSERTION FAILED!\n"
            f"URL: {response.url}\n"
            f"Expected: {expected_status}\n"
            f"Actual: {actual_status}\n"
            f"Response Body: {response.text}\n"
        )
        logger.error(error_msg)
        
        allure.attach(
            response.text, 
            name="Error Response Body", 
            attachment_type=allure.attachment_type.JSON
        )   
        assert actual_status == expected_status, f"Expected {expected_status}, but got {actual_status}. Body: {response.text}"
    return response
