import requests

def convert(amount, base_currency, target_currency):
    url = f"https://api.frankfurter.dev/v2/rate/{base_currency}/{target_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rate']
        total = amount * rate
        print(f"{amount} {base_currency} = {total:.2f} {target_currency} on rate = {rate}")

    else:
        print('Error fetching rates')




amount = float(input('Enter the total convertible amount --> '))

base_currency = input('enter the base currency, ex: INR, USD, etc --> ')
target_currency = input('enter the target currency type to convert --> ')

convert(amount, base_currency, target_currency)
