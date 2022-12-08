from django.urls import path
from api.views import get_tokenView

urlpatterns = [
	path('', get_tokenView)
]