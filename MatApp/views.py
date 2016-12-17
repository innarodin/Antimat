import sqlite3

from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from djantimat.helpers import PymorphyProc
import json

class DBConnection: #singleton
    instance = None
    connection = None
   # cursor = None

    def __new__(cls):
        print('in new')
        if DBConnection.instance is None:
            DBConnection.instance = object.__new__(cls)
        return DBConnection.instance

    def __init__(self):
        print('in init')
        if self.connection is None:
            try:
                self.connection = sqlite3.connect('db.sqlite3')
                print('Database connection opened.')
            except sqlite3.DatabaseError as db_error:
                print("Error :\n{0}".format(db_error))

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
            print('Database connection closed.')


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
    def check1(request):
        try:
            if request.method == "POST" and request.is_ajax():
                inputText = request.POST['text']
                context = {
                    "text" : PymorphyProc.wrap(inputText)
                }
                return HttpResponse(json.dumps(context))
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
            AddNewWords.saveInDB(text)
            i = i + 1
      #  conn.close()
        return render(request, "MatApp/home.html")

    @staticmethod
    def saveInDB(text): #я хз почему не работает
        print('In save')
        conn = DBConnection()
        print(conn)

        print("before cursor")
        cursor = conn.connection.cursor()
        print("after cursor")

        cursor.execute('INSERT INTO djantimat_slang (word) VALUES (?)', (text,))
        print("after insert")

        conn.connection.commit()
        print("after commit")

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
    def addingWord(request):
        return render(request, 'MatApp/addingWord.html')