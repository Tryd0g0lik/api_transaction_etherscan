from django import forms

class GetTokenOfMainForms(forms.Form):
	"""
	TODO: get data forms of the main site page
	"""
	token_user = forms.CharField(
		label="token_user",
		max_length=150,
	)

	adress_for_search = forms.CharField(
		label="adress_for_search",
		max_length=150,
	)

	method_transactions = forms.CharField(
		label="method_transactions",
		max_length=150,
	)

