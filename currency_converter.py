from requests import get 
from pprint import PrettyPrinter

BASE_URL = 'https://free.currconv.com/'
API_KEY = ''

printer = PrettyPrinter()

endpoint = f'api/v7/currencies?apiKey={API_KEY}'
