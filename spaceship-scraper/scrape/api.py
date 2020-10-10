import requests

base_url = "https://api.spaceshipinvest.com.au/v0/external"


def get_investment_summary(session: requests.Session):

    url = f"{base_url}/saver/account/investment-summary"

    response = session.get(url)
    json = response.json()

    return json


def get_investment_history(session: requests.Session):

    url = f"{base_url}/saver/account/investment-history"

    response = session.get(url)
    json = response.json()

    return json


def get_unit_prices(session: requests.Session, portfolio="UNIVERSE", date="1970-01-01"):

    url = f"{base_url}/saver/unit-price/graph?portfolio={portfolio}&date={date}"

    response = session.get(url)
    json = response.json()

    return json
