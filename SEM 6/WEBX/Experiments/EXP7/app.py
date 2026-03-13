from flask import Flask, render_template, request

app = Flask(__name__)

exchange_rates = {
    'USD': 1.0,      
    'INR': 92.45,    
    'GBP': 0.75,     
    'SAR': 3.75,     
    'CNY': 6.87      
}


def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return round(converted_amount, 2)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        
        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            return render_template('index.html', error="Invalid currency selected")
        
        result = convert_currency(amount, from_currency, to_currency)
        
        currency_symbols = {
            'USD': '$',
            'INR': '₹',
            'GBP': '£',
            'SAR': '﷼',
            'CNY': '¥'
        }
        
        return render_template('index.html', 
                             result=result,
                             amount=amount,
                             from_curr=f"{currency_symbols[from_currency]} {from_currency}",
                             to_curr=f"{currency_symbols[to_currency]} {to_currency}")
    
    except ValueError:
        return render_template('index.html', error="Please enter a valid amount")
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)