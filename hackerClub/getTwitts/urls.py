from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$', views.getUser.as_view(), name="user"),
	url(r'^archivo', views.get_file, name="archivo"),
]