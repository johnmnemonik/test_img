from django.urls import path

from img import views

urlpatterns = [
	path('img/', views.index, name='index'),
	path('resize/', views.resize, name='resize'),
]