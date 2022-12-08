from web3 import Web3 as web # EthereumTesterProvider

_API = '5PNDPQY793WFZ3HMK9TC8MNYXI888P84AK'
ADRESS = '0x118ee078c3625144e3a942566fbc84f187f8c8b6'
_api = 'api-goerli.etherscan.io/api?module=account&action=txlistinternal&address=%s&startblock=5&endblock=99999999&page=0&offset=5&sort=asc&apikey=%s'\
	% (ADRESS, _API)

# class Teslo():
with requests.Session() as s:
	# print(s.get('https://' + _api).json()['result'])
	pprint(s.get('https://' + _api).json()['result'])