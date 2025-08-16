from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('evaluate/', views.evaluate_answers, name='evaluate'),
]