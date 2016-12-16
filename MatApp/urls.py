from django.conf.urls import url, include
from MatApp import views

urlpatterns = [
    url(r'^$', views.CheckMat.home, name='home'),
    url(r'^check$', views.CheckMat.check, name='check'),
    url(r'^check1$', views.CheckMat.check1, name='check1'),
    url(r'^addWord', views.AddNewWords.addWord, name='addWord'),
    url(r'^addDict', views.AddNewWords.jsonSave, name='addDict'),
    url(r'^addingWord', views.AddNewWords.addingWord, name='addingWord'),
    url(r'^testFunc$', views.TestClass.testFunc, name='testFunc'),
]