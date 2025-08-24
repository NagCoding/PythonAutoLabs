import requests
import logging
import time

logger = logging.getLogger(__name__)

def test_update_settings(config):
    get_url = f"{config.env_url}/settings?includes=portalSetting,country"
    update_url = f"{config.env_url}/settings/{config.store}"
    req_params = {"api_token" : config.store_api_token}

    #get settings function
    def get_settings():
        # GET API Call
        logger.info(f"Sub Function started")
        get_response = requests.get(get_url, params=req_params)
        get_res_json = get_response.json()

        email = get_res_json.get("data", [])[0].get("email")
        updated_at = get_res_json.get("data", [])[0].get("updated_at")
        logger.info(f"Sub Function ended")
        return email, updated_at, get_response.status_code

    email, updated_at, status_code = get_settings()
    logger.info(f"GET settings response code is - {status_code}")
    logger.info(f"Email from GET API response is - {email}")
    logger.info(f"The Last updated_at is  - {updated_at}")

    body = {"email":"nagendrababu.c@foodhub.com"}

    #UPDATE API Call
    update_response = requests.put(update_url,json=body,params=req_params)
    update_res_json = update_response.json()
    outcome = update_res_json.get("outcome")

    logger.info(f"UPDATE settings response code is - {update_response.status_code}")
    logger.info(f"UPDATE settings response outcome is - {outcome}")

    #Call get_settings() to fetch the latest values
    time.sleep(2)
    email1, updated_at1, status_code1 = get_settings()
    logger.info(f"GET settings response code after UPDATE call is - {status_code1}")
    logger.info(f"Email from GET API response after UPDATE call is - {email1}")
    logger.info(f"The updated_at value after UPDATE call is  - {updated_at1}")

    assert email1 == "nagendrababu.c@foodhub.com"

