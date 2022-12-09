from datetime import time
import requests as regs
from django.utils import dateformat

def _get_dataApi(
	_adress_for_search: str,
	_token_user: str,
	_method_transactions: str = None,
	_startblock: int = 0,
	) -> list:

	if _method_transactions == 'None' or\
		_method_transactions == '':
		api = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&address=%s&startblock=%s&endblock=99999999&page=1&offset=10&sort=asc&apikey=%s'\
		% (  _token_user, _startblock, _adress_for_search,)

		api = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&address=%s&startblock=%s&endblock=99999999&page=1&offset=10&sort=asc&apikey=%s'\
		% (  _token_user, _startblock, _adress_for_search,)

		_api_response = regs.get(api)  #  getting data
		_api_response = _api_response.json()['result']

		if len(_api_response) > 100: #  look the last 100 positions if the list contains more 100 positions
			return _api_response[-99: ]

		return _api_response

	else:
		...
	return

def _records_data_inFiles(*args):
	"""
	TODO Record dataset from user data form
	:param args:
	:return: Creating of one or three files *.txt
	"""

	if len(args[0]) >= 1:
		f = open('apps_web_scraping/api/files/token.txt', 'w')
		f.write(args[0][0])
		f.close()

	if len(args[0]) >= 2:
		f = open('apps_web_scraping/api/files/adress.txt', 'w')
		f.write(args[0][1])
		f.close()

	if len(args[0]) == 3:
		f = open('apps_web_scraping/api/files/method.txt', 'w')
		f.write(args[0][2])
		f.close()

	else:
		return 'You need checking the data'
	return

def _reads_data_files():
	token_user: str  = None
	adress_for_search: str = None
	method_transactions: str = None

	import os
	_f_list = []

	_s = os.walk('apps_web_scraping/api/files/')
	for name_file in _s: _f_list = name_file[2]

	for _f in _f_list:
		i = _f_list.index(_f)
		_read = open('apps_web_scraping/api/files/%s'\
		             % (_f_list[i],), 'r')

		_read_data = _read.read()
		_read.close()

		# print(f"_f_list: {_f_list}")
		if 'token' in _f_list[i]: token_user = str(_read_data)
		if 'adress' in _f_list[i]: adress_for_search = str(_read_data)
		if 'method' in _f_list[i]: method_transactions = str(_read_data)

	return [token_user, adress_for_search, method_transactions]

def _restart_time() -> bool:
	from datetime import datetime
	_time = True
	_datetime_response = None

	_datetime_response = datetime.now()
	_start_time = (_datetime_response.time().strftime("%I:%M:%S"))

	_start_time = datetime.strptime(_start_time, "%I:%M:%S").time()

	while _time:
		_now_time = None
		_now_time_n = (datetime.now().time().strftime("%I:%M:%S"))
		_now_time = datetime.strptime(_now_time_n, "%I:%M:%S").time()

		if _now_time.second - _start_time.second == 60:
			_time = False
			return True
	return False




