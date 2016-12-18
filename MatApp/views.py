import sqlite3

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

    @staticmethod
    def checkForAjax(request):
        try:
            if request.method == "POST" and request.is_ajax():
                inputText = request.POST['text']
                context = {
                    'text': PymorphyProc.wrap(inputText),
                    "isError": "false"
                }
                return HttpResponse(json.dumps(context))
        except:
            return HttpResponse(json.dumps({"isError": "true", "errorMsg":'Ошибка проверки'}))

class AddNewWords:

    @staticmethod
    def jsonSave(request):
        with open('F:\\Users\\Admin\\Desktop\\file.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        #data = json.loads('[{ "word": "\u0430\u0431\u043e\u0440\u0442\u043c\u0430\u0445\u0435\u0440", "pk": 1},{ "word": "\u0430\u043d\u0430\u043b", "pk": 2}]')
        for i in data:
            text = data[i]['word']
            AddNewWords.saveInDB(text)
      #  conn.close()
        return render(request, "MatApp/home.html")


    @staticmethod
    def saveInDB(text):
        b = Slang(word=text.lower())
        b.save()


    @staticmethod
    def addWord(request):
        try:
            if request.method == "POST":
                inputText = request.POST['word']
                AddNewWords.saveInDB(inputText)
                context = {
                    'newWord': inputText
                }
                return render(request, "MatApp/addingWord.html", context)
        except:
            return HttpResponse('Слово уже есть в базе')

    @staticmethod
    def addWordForAjax(request):
        # print("before try")
        try:
            # print("before if")
            if request.method == "POST" and request.is_ajax():
                inputText = request.POST['word']
                # print(inputText)
                AddNewWords.saveInDB(inputText)
                context = {
                    "isError" : "false",
                    'newWord': inputText
                }
                # print(context)
                return HttpResponse(json.dumps(context))
        except:
            return HttpResponse(json.dumps({"isError" : "true","errorMsg": 'Ошибка выполнения: Слово уже есть в базе'}))


    @staticmethod
    def addingWord(request):
        return render(request, 'MatApp/addingWord.html')