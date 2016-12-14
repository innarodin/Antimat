from django.conf.urls import url, include
from MatApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^check$', views.check, name='check'),
    url(r'^addWord', views.addWord, name='addWord'),
    url(r'^addDict', views.jsonSave, name='addDict'),
    url(r'^addingWord', views.addingWord, name='addingWord'),
]