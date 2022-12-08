from pprint import pprint

from django.shortcuts import render

# Create your views here.

def get_tokenView(request):
	if request.method == 'GET':
		# pprint(request.GET.__dict__)
		print(request._messages)
	return render(request, 'api/index.html', context={})