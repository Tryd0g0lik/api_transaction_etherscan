import requests as regs

_API = '5PNDPQY793WFZ3HMK9TC8MNYXI888P84AK'
ADRESS = '0x118ee078c3625144e3a942566fbc84f187f8c8b6'
_api = 'api-goerli.etherscan.io/api?module=account&action=txlistinternal&address=%s&startblock=5&endblock=99999999&page=0&offset=5&sort=asc&apikey=%s'\
	% (ADRESS, _API)

def _get_dataApi(
	adress_for_search: str,
	token_user: str,
	method_transactions: str = None):

	if method_transactions == 'None' or\
		method_transactions == '':
		api = 'https://api-goerli.etherscan.io/api?module=account&action=txlist&address=%s&startblock=5&endblock=99999999&page=1&offset=10&sort=asc&apikey=%s'\
		% ( token_user, adress_for_search,)
		api_response = regs.get(api)  #  getting data

		return api_response
	else:
		...
	return

def _records_data_inFiles(*args):
	"""
	TODO Record dataset from user data form
	:param args:
	:return: Creating of one or three files *.txt
	"""

	if args[0] == True\
		and len(args[0]) >= 1:
		print(f"args[0]: {args[0][0]}")
		f = open('apps_web_scraping/api/files/token.txt', 'w')
		f.write(args[0][0])
		f.close()

	if args[0][1] == True\
		and len(args[0]) >= 2:
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