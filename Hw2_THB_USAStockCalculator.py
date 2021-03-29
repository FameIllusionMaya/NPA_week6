import urllib.parse
import requests
import json

print("Stock price calculator THB -> stock amount")
while True:
    print()
    stock_symbol = input("Input stock symbol : ")
    money_thb = float(input("Input amount of money(THB) : "))

    key = "c1go7qf48v6v8dn0ddeg"
    main_api_stock = 'https://finnhub.io/api/v1/quote?'
    url_stock = main_api_stock + urllib.parse.urlencode({"token":key, "symbol":stock_symbol})
    res_stock = requests.get(url_stock)
    result_stock = res_stock.json()

    main_api_currency = "https://api.exchangeratesapi.io/latest?"
    url_currency = main_api_currency + urllib.parse.urlencode({"base" : "USD", "symbols":"THB"})
    res_currency = requests.get(url_currency)
    result_currency = res_currency.json()

    current_price = result_stock['c']
    usdthb_value = result_currency["rates"]["THB"]
    money_usd = money_thb/usdthb_value

    print("Current price : %.2f USD" %(current_price))
    print("1 USD now equal : %f THB" %(usdthb_value))
    print("You can buy %s for %d unit(s)" %(stock_symbol, money_usd/current_price))
