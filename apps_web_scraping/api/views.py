from pprint import pprint
# from forms import GetTokenOfMainForms
from django.shortcuts import render
from api.forms import GetTokenOfMainForms

def get_tokenView(request):
	if request.method == 'POST':
		print(request._post['token_user'])
		print(request._post['adress_for_search'])
		print(request._post['method_transactions'])
		return render(request, 'api/index.html', context={})
	else:
		form = GetTokenOfMainForms()
		return render(request, 'api/index.html', context={'form' : form})


