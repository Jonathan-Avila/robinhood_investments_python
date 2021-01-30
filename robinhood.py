#!/usr/bin/env python3
import robin_stocks as robin
import robinhood_config as cfg
import pyotp
import sys

login = robin.login(cfg.get_email, cfg.get_passwd, mfa_code=cfg.get_mfa_code)

def quote(ticker):
    try:
        for element in ticker:
            element = element.upper()
            r = robin.get_latest_price(element)
            print(element.upper() + " $" + "{:.2f}".format(float(r[0])))
    except TypeError:
        print("Not a valid ticker symbol")

def buy(ticker, amount):
    r = robin.order_buy_fractional_by_price(ticker, int(amount))
    print(r)

def sell(ticker, amount):
    r = robin.order_sell_fractional_by_price(ticker, int(amount))
    print(r)

if __name__ == "__main__":

    ticker = sys.argv[1:]

    if len(ticker) == 3:
        ticker[0] = ticker[0].upper()
        if ticker[0] == "BUY":
            buy(ticker[1], ticker[2])
        elif ticker[0] == "SELL":
            sell(ticker[1], ticker[2])
        else:
            quote(ticker)
    else:
        quote(ticker)
