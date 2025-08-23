import requests
import logging
from POSTRequest_test import test_oauthtoken

logger = logging.getLogger(__name__)

def test_get_store(config):
    logger.info(f"GETRequest started running..")
    url = f"{config.env_url}/consumer/store"
    req_params = {"app_name": config.app_name}
    req_headers = config.headers.copy()
    logger.info("Calling oauthtoken function..")
    access_token = test_oauthtoken(config)
    req_headers["Authorization"] = f"Bearer {access_token}"
    #logger.info("Called oauth")
    req_headers["store"] = config.store
    req_headers["franchise"] = config.franchise
    logger.info(f"Calling Store API..")

    response = requests.get(url,params=req_params,headers=req_headers)
    logger.info(f"Store API has been called")
    logger.info(f"Response status code is - {response.status_code}")
    json_response = response.json()
    store_id = json_response.get("id")
    store_host = json_response.get("host")
    logger.info(f"Store ID from response is - {store_id}")
    logger.info(f"Store Host from response is - {store_host}")
    logger.info(f"Access Token from other function is - {access_token}")
    logger.info(f"GETRequest executed..")




