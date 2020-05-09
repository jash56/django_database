from django.urls import path
from . import views

urlpatterns = [
	path('', views.form, name = 'form'),
	path('registeration', views.registeration, name = 'registeration'),
	path('login1', views.login1, name = 'login1'),
	path('marvel', views.marvel, name = 'marvel'),
	path('logout', views.logout, name = 'logout'),

]