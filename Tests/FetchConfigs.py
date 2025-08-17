import requests
import logging


logger = logging.getLogger(__name__)

def test_get_store(config):
    url = f"{config.env_url}/consumer/store"
    headers = config.headers.copy() # copy to avoid modifying global config
    headers["franchise"]= config.franchise
    headers["store"] = "8955411"
    #headers["passport"] = config.passport
    params = {"app_name" : config.app_name}

    store_res = requests.get(url, params=params, headers= headers)
    logger.info(f"API response status code is - {store_res.status_code}")
    assert store_res.status_code == 200

