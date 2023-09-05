import requests



def get_currency_codes():
    """Gets 3 letter currency codes, and puts them in a list"""

    symbol_res = requests.get('https://api.exchangerate.host/symbols')
    symbol_data = symbol_res.json()
    symbols = symbol_data['symbols']

    codes = {}

    for key, value in symbols.items():
        codes[key] = value['description']


    return codes



def check_invalidity(start, end, amount):
    """Checks if form fields are invalid...
    
    if so, return the correct flash message"""


    symbol_res = requests.get('https://api.exchangerate.host/symbols')
    symbol_data = symbol_res.json()
    symbols = symbol_data['symbols']

    result = ''

    if (not start or not end or not amount):
        result = 'Please fill out all fields'

    if start and start.upper() not in symbols:
        result = f'"{start}" is an invalid currency code'
    
    if end and end.upper() not in symbols:
        result = f'"{end}" is an invalid currency code'
    
    if (start and start.upper() not in symbols) and (end and end.upper() not in symbols):
        result = f'"{start}" and "{end}" are invalid currency codes'

    return result