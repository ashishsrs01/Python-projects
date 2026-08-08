import requests

def convert(amount, base_currency, target_currency):
    url = f"https://api.frankfurter.dev/v2/rate/{base_currency}/{target_currency}"
    try:
        response = requests.get(url, timeout=8)
        response.raise_for_status()
        data = response.json()
        rate = data['rate']
        total = amount * rate
        print(f"{amount} {base_currency} = {total:.2f} {target_currency} on rate = {rate}")
    except requests.exceptions.HTTPError:
        print('Error fetching rates: server returned an invalid response.')
    except requests.exceptions.RequestException as exc:
        print('Network error while fetching rates:', exc)
    except ValueError:
        print('Error parsing response from the currency service.')
    except KeyError:
        print('Unexpected response format from the currency service.')


if __name__ == '__main__':
    try:
        amount = float(input('Enter the total convertible amount --> '))
    except ValueError:
        print('Please enter a valid numeric amount.')
    else:
        base_currency = input('enter the base currency, ex: INR, USD, etc --> ')
        target_currency = input('enter the target currency type to convert --> ')
        convert(amount, base_currency, target_currency)
