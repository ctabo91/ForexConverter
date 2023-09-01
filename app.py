from flask import *
from functions import check_invalidity, get_currency_codes
import requests
from forex_python.converter import CurrencyCodes



app = Flask(__name__)
app.config['SECRET_KEY'] = 'money money money'




codes = get_currency_codes()



@app.route('/')
def show_currency_converter():
    """displays currency converter form"""

    return render_template('forex-converter.html', codes=codes)


@app.route('/conversion')
def show_conversion():
    """makes sure all form fields are filled out correctly
    
    if fields not filled out correctly, shows appropriate message to user and resets form
    
    if filled out correctly, shows converted currency rate"""


    start = request.args.get('start-curr')
    end = request.args.get('end-curr')
    amount = request.args.get('amount')

    invalid = check_invalidity(start, end, amount)

    if invalid:
        flash(invalid)
        return redirect('/')
    

    url = f'https://api.exchangerate.host/convert?from={start}&to={end}&amount={amount}&places=2'
    res = requests.get(url)
    data = res.json()
    result = data['result']
    full_result = f'{CurrencyCodes().get_symbol(end.upper())} {result}'

    return render_template('forex-converter.html', result=full_result, codes=codes)


