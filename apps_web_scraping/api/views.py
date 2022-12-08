from pprint import pprint
import requests as regs
from django.shortcuts import render
from api.forms import GetTokenOfMainForms
from api.moduls.functions import _get_dataApi, _records_data_inFiles, _reads_data_files


def get_tokenView(request):
	if request.method == 'POST' and\
		request._post['token_user'] != "" and\
		request._post['token_user'] != None:
		#  get user's data
		token_user = request._post['token_user']
		adress_for_search = request._post['adress_for_search']
		method_transactions = request._post['method_transactions']

		#  records user's data in files
		if method_transactions:
			user_data_list = [str(token_user), str(adress_for_search), str(method_transactions)]
		else:
			user_data_list = [token_user, adress_for_search]
		print(f"user_data_list: {user_data_list}")
		_records_data_inFiles(user_data_list) #  records data in files
		_read_user_data = _reads_data_files()

		#  get and send api data
		api_data = _get_dataApi(token_user, adress_for_search, method_transactions, )
		api_header = dict(api_data[0]).keys()
		print(f"api_header: {list(api_header)}")
		return render(request, 'api/index.html', context={'form': 'True', 'api_header': list(api_header), 'api_data':
			api_data}, )



	else:
		GetTokenOfMainForms()
		return render(request, 'api/index.html', context={'form': 'None'})
