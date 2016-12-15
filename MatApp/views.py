import sqlite3

import sys
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from djantimat.helpers import PymorphyProc
import json

from djantimat.models import Slang

class CheckMat:
    @staticmethod
    def home(request):
        return render(request, 'MatApp/home.html')

    @staticmethod
    def check(request):
        try:
            if request.method == "POST":
                inputText = request.POST['text']
                context = {
                    'text': PymorphyProc.wrap(inputText)
                }
                return render(request, "MatApp/home.html", context)
        except:
            return HttpResponse('Ошибка проверки')

class TestClass:
    @staticmethod
    def testFunc(request):
        try:
            if request.method == "POST" and request.is_ajax():
                postdata = request.POST["testWord"]
            return HttpResponse(postdata)
        except:
            return HttpResponse("mistake")

class AddNewWords:
    @staticmethod
    def jsonSave(request):
        with open('F:\\Users\\Admin\\Desktop\\file.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        #data = json.loads('[{ "word": "\u0430\u0431\u043e\u0440\u0442\u043c\u0430\u0445\u0435\u0440", "pk": 1},{ "word": "\u0430\u043d\u0430\u043b", "pk": 2}]')
        i = 0
        while data[i + 1] != None:
            text = data[i]['word']
            AddNewWords().saveInDB(text)
            i = i + 1
        conn.close()
        return render(request, "MatApp/home.html")

    @staticmethod
    def saveInDB(text):
      #  try:
             conn = AddNewWords().connDB()
             c = conn.cursor()
             c.execute('INSERT INTO djantimat_slang (word) VALUES (?)', (text,))
             conn.commit()
             conn.close()
      #  except:
      #      return HttpResponse('Слово уже есть в базе')


    @staticmethod
    def connDB():
        try:
            conn = sqlite3.connect('db.sqlite3')
            return conn
        except ConnectionError:
            return HttpResponse('Ошибка подключения к базе')

    @staticmethod
    def addWord(request):
        try:
            if request.method == "POST":
                inputText = request.POST['word']
                AddNewWords().saveInDB(inputText)
                context = {
                    'newWord': inputText
                }
                return render(request, "MatApp/addingWord.html", context)
        except:
            return HttpResponse('Слово уже есть в базе')

    @staticmethod
    def addingWord(request):
        return render(request, 'MatApp/addingWord.html')