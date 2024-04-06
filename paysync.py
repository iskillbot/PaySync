import requests

def make_request(url, params = None, json_data = None):
    try:
        response = requests.get(url, params = params, json = json_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": e}

def generate_card(client = None, amount = None, currency = None):
    if client is None:
        return {"error": "Укажите номер клиента"}
    if amount is None:
        return {"error": "Укажите сумму заявки"}
    if currency is None:
        return {"error": "Укажите валюту"}
    
    url = f"https://paysync.cc/api/client{client}/amount{amount}/currency{currency}"
    return make_request(url)

def generate_crypto_address(ticker = None, address = None, callback = None):
    if ticker is None:
        return {"error": "Укажите символьный код криптовалюты"}
    if address is None:
        return {"error": "Укажите криптовалютный адрес"}
    if callback is None:
        return {"error": "Укажите Callback URL"}

    url = "https://paysync.cc/api/crypto"
    params = {"ticker": ticker, "address": address, "callback": callback}
    return make_request(url, params = params)

def create_invoice(client = None, amount = None, currency = None):
    if client is None:
        return {"error": "Укажите номер клиента"}
    if amount is None:
        return {"error": "Укажите сумму заявки"}
    if currency is None:
        return {"error": "Укажите валюту"}

    url = f"https://paysync.cc/create_invoice/{client}/{amount}/{currency}"
    return make_request(url)

def make_payment(api_key = None, amount = None, address = None):
    if api_key is None:
        return {"error": "Укажите ваш API KEY"}
    if amount is None:
        return {"error": "Укажите сумму для вывода"}
    if address is None:
        return {"error": "Укажите криптовалютный адрес"}

    url = "http://paysync.cc/send/usdt"
    data = {"apikey": api_key, "amount": amount, "address": address}
    return make_request(url, json_data = data)

def get_transactions(api_key = None):
    if api_key is None:
        return {"error": "Укажите ваш API KEY"}

    url = f"https://paysync.cc/get_transactions/{api_key}"
    return make_request(url)

def get_balance(api_key = None):
    if api_key is None:
        return {"error": "Укажите ваш API KEY"}

    url = f"https://paysync.cc/get_balance/{api_key}"
    return make_request(url)

def get_trade_status(trade_id = None):
    if trade_id is None:
        return {"error": "Укажите номер заявки"}

    url = f"https://paysync.cc/gettrans/{trade_id}"
    return make_request(url)


test = get_balance(40627933)
print(test)