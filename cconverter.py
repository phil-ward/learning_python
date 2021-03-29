import requests, json


def request_float_rate(user_current_currency):
    currencies = requests.get('https://www.floatrates.com/daily/{}.json'.format(user_current_currency.lower()))
    return currencies.json()


def check_cache(currency_to_check):
    cache_hit = False
    with open('cache.json', 'r+', encoding='utf-8') as cache_read_file:
        temp_cache = json.load(cache_read_file)
        if currency_to_check in temp_cache.keys():
#            print(temp_cache[currency_to_check].get('rate'))
            return temp_cache[currency_to_check].get('rate')
    if not cache_hit:
        return False

def write_new_cache(currency_to_check, currency_json):
    with open('cache.json', 'r', encoding='utf-8') as cache_file_to_append:
        temp_cache = json.load(cache_file_to_append)
    temp_cache[currency_to_check] = currency_json.get(currency_to_check)
    with open('cache.json', 'w', encoding='utf-8') as cache_file_to_append:
        json.dump(temp_cache, cache_file_to_append)


cache = {}
current_currency = input()
current_currency_json = request_float_rate(current_currency)
with open('cache.json', 'w', encoding='utf-8') as cache_file:
    cache['usd'] = current_currency_json.get('usd')
    cache['eur'] = current_currency_json.get('eur')
    json.dump(cache, cache_file)
while True:
    requested_currency = input()
    if requested_currency == '':
        break
    currency_amount = float(input())
    print("Checking the cache...")
    cache_check = check_cache(requested_currency.lower())
    if cache_check:
        print('Oh! It is in the cache!')
    elif not cache_check:
        print('Sorry, but it is not in the cache!')
        write_new_cache(requested_currency.lower(), current_currency_json)
    converted_amount = currency_amount * current_currency_json.get(requested_currency.lower())['rate']
    print('You received {} {}.'.format(round(converted_amount, 2), requested_currency))
