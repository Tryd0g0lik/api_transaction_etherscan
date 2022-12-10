import json
import requests as regs

def get_dataApi(*args, _startblock: int = 0) -> list:
	"""
	TODO: Gettin API-data and :
	- first it's spend tada on front user-page
	- second it's update api-tada in loop.

	:param args:It's key data the token, adress, method for a filter transaction.
	:param _startblock: this's Number block tor beginning to get data
	:return:last 100 position for a transaction/

	"""
	#  Geting data is token, adress
	_method_transactions ='None'
	if type(args) == tuple :
		_adress_for_search: str = args[0][0]
		_token_user: str = args[0][1]
	else:
		_adress_for_search: str = args[1]
		_token_user: str = args[0]

	if len(args) == 3 and\
		type(args) == tuple:
		_method_transactions = args[2]

	elif len(args) == 3:
			_method_transactions = args[2]

	if _method_transactions == 'None' or \
		_method_transactions == '':

		api = 'https://api-goerli.etherscan.io/api?module=account&action=txlistinternal&address=%s&startblock=%s&endblock=99999999&page=1&offset=10&sort=asc&apikey=%s' \
		      % (  _token_user, _startblock, _adress_for_search,)

		_api_response = regs.get(api)  #  getting data
		_api_response = _api_response.json()['result']

		with open('apps_web_scraping/api/files/api_data.json', 'w') as write_file:
			json.dump(_api_response, write_file)

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

def reads_data_files() -> list:
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


def file_records():
	"""
	:return: the API-data will be update everu 60 seconds
	"""
	from datetime import datetime
	_event = True
	_datetime_response = None
	_start_time = None

	_datetime_response = datetime.now()
	_start_time = (_datetime_response.time().strftime("%I:%M:%S"))
	_start_time = datetime.strptime(_start_time, "%I:%M:%S").time()


	while _event:
		_now_time = None
		_now_time_n = (datetime.now().time().strftime("%I:%M:%S"))
		_now_time = datetime.strptime(_now_time_n, "%I:%M:%S").time()

		_time = (_now_time.second - _start_time.second)
		if _time == 59 or\
			_time == (-1):
			list_key_data = reads_data_files()
			get_dataApi(list_key_data)


			_now_time_n = (datetime.now().time().strftime("%I:%M:%S"))
			_start_time = _now_time = datetime.strptime(_now_time_n, "%I:%M:%S").time()




