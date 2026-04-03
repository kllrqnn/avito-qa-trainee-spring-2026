
def get_id_from_response(response):
    """
    Парсинг ID
    """
    status_text = response.json().get("status", "")
    return status_text.split("- ")[-1] if "- " in status_text else None