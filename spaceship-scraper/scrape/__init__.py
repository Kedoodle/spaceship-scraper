import requests


def get_session():

    login_url = "https://api.spaceshipinvest.com.au/v0/external/user/login"
    session = requests.session()
    response = session.post(login_url)

    return session
