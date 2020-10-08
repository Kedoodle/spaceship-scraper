import logging
import requests

import config

username = config.username
password = config.password


def get_session():

    login_url = "https://api.spaceshipinvest.com.au/v0/external/user/login"
    session = requests.session()

    try:

        response = session.post(login_url, auth=(username, password))
        response.raise_for_status()

        bearer_token = response.json()["auth"]["auth_token"]
        session.auth = (bearer_token, "")

    except requests.exceptions.HTTPError:

        logging.error("Invalid credentials. Check SPACESHIP_USERNAME and SPACESHIP_PASSWORD environment variables.")
        exit(1)

    return session
