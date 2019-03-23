from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.my_index, name='my_index'),
]
