from django.shortcuts import render
from api.forms import GetTokenOfMainForms
from api.moduls.decorators import api_data_rewriteDecorators
from api.moduls.functions import get_dataApi, _records_data_inFiles

@api_data_rewriteDecorators
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

		_records_data_inFiles(user_data_list) #  records data in files

		#  get and send api data
		api_data = get_dataApi(user_data_list)
		api_header = dict(api_data[0]).keys()

		return render(request, 'api/index.html', context={'form': 'True', 'api_header': list(api_header), 'api_data':
			api_data}, )

	else:
		GetTokenOfMainForms()
		return render(request, 'api/index.html', context={'form': 'None'})

