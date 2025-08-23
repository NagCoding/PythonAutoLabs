import requests
import logging

logger = logging.getLogger(__name__)

def test_oauthtoken(config):
    logger.info(f"POSTRequest started running..")
    url = f"{config.env_url}/oauth/client"
    headers = config.headers.copy()
    body = {
    "name": "unknown",
    "platform_id": 1,
    "product_id": "14",
    "auth_type": "CONSUMER",
    "uuid": "87d425f2-9f90-4000-a57b-1506d717a64fadO"
        }


    response = requests.post(url,json=body,headers=headers)
    assert response.status_code == 200
    logger.info(f"Oauth API response status code is - {response.status_code}")
    #logger.info(response.headers)

    json_response = response.json()
    #logger.info(f"The Oauth response is : {json_response}")

    oauth_access_token = json_response.get("data",{}).get("access_token")
    logger.info(f"Access Token is -: {oauth_access_token}")
    return oauth_access_token

logger.info(f"POSTRequest executed..")





