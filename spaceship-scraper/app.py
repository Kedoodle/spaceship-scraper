import scrape.api
import scrape.auth


def main():

    session = scrape.auth.get_session()

    investment_summary = scrape.api.get_investment_summary(session)
    investment_history = scrape.api.get_investment_history(session)
    unit_prices = scrape.api.get_unit_prices(session)["unit_prices"]

    aud_balance = float(investment_summary["aud_balance"])
    invested = float(investment_summary["aud_total_invested"])
    referrals = float(investment_summary["aud_total_referrals"])
    promotions = float(investment_summary["aud_total_promotions"])
    withdrawn = float(investment_summary["aud_total_withdrawn"])
    aud_return = float(investment_summary["aud_market_return"])
    unit_balance = float(investment_summary["unit_balance"])
    latest_unit_price = float(unit_prices[-1]["aud_price"])
    latest_date = unit_prices[-1]["date"]

    deposits = invested + referrals + promotions
    average_unit_cost = (invested - withdrawn) / unit_balance
    current_return_percentage = (latest_unit_price - average_unit_cost) / average_unit_cost * 100

    print(f"""Investment summary as at {latest_date}

Balance: ${aud_balance}
    Deposits: ${deposits}
        Invested: ${invested}
        Referrals: ${referrals}
        Promotions: ${promotions}
    Withdrawals: ${withdrawn}
    Return: ${aud_return}
Unit balance: {unit_balance} units

Average unit cost: ${round(average_unit_cost, 6)}
Current unit cost: ${latest_unit_price} ({round(current_return_percentage, 2)}%)""")


if __name__ == '__main__':
    main()
