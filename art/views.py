from django.shortcuts import render
from requests import get
import json


# Create your views here.
def main(request):
    return render(request, 'main.html')


def demand(request):
    return render(request, 'demand.html')


def geography(request):
    return render(request, 'geography.html')


def skills(request):
    return render(request, 'skills.html')


def vacancy(request):
    params = {
        'text': 'NAME:DevOps-инженер', # Текст фильтра
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 8, # Кол-во вакансий на 1 странице
        'only_with_salary': True,
        #'currency': 'NAME:Rur',
        'date_from': "2022-12-20T21:00:00",
        'date_to': "2022-12-22T10:00:00"
}


    req = get('https://api.hh.ru/vacancies', params) # Посылаем запрос к API
    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    c = json.loads(data)
    print(c)
    return render(request, 'vacancy.html', c)
