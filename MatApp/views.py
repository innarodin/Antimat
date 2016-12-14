import sqlite3
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from djantimat.helpers import PymorphyProc
import json

from djantimat.models import Slang

def home(request):
    return render(request, 'MatApp/home.html')


def check(request):
    if request.method == "POST":
        inputText = request.POST['text']
        context = {
            'text': PymorphyProc.wrap(inputText)
        }
        return render(request, "MatApp/home.html", context)
    else:
        return HttpResponse('Error')


def jsonSave(request):
    with open('F:\\Users\\Admin\\Desktop\\file.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    #data = json.loads('[{ "word": "\u0430\u0431\u043e\u0440\u0442\u043c\u0430\u0445\u0435\u0440", "pk": 1},{ "word": "\u0430\u043d\u0430\u043b", "pk": 2}]')
    i = 0
    while i < 3980:
        text = data[i]['word']
        saveInDB(text)
        i = i + 1
    conn.close()
    return render(request, "MatApp/home.html")


def saveInDB(text):
     conn = connDB()
     c = conn.cursor()
     c.execute('INSERT INTO djantimat_slang (word) VALUES (?)', (text,))
     conn.commit()
     conn.close()


def connDB():
    conn = sqlite3.connect('db.sqlite3')
    return conn


def addWord(request):
    if request.method == "POST":
        inputText = request.POST['word']
        saveInDB(inputText)
        context = {
            'newWord': inputText
        }
        return render(request, "MatApp/home.html", context)
    else:
        return HttpResponse('Error')
