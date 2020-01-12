from django.conf.urls import url
from our_parea import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^food/', views.food, name='food'),
    url(r'^culture/', views.culture, name='culture'),
]

