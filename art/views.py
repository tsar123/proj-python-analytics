from django.shortcuts import render
from requests import get
import json

from art.models import *


# Create your views here.
def main(request):
    return render(request, 'main.html')


def demand(request):
    return render(request, 'demand.html')


def geography(request):
    geo = Geography.objects.all()
    vac = VacancyRate.objects.all()
    c = {
        'ge': geo,
        'va': vac
    }
    print(c)
    return render(request, 'geography.html', c)


def skills(request):
    return render(request, 'skills.html')


def vacancy(request):
    params = {
        'text': 'NAME:DevOps-инженер', # Текст фильтра
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 8, # Кол-во вакансий на 1 странице
        'only_with_salary': True,
        'date_from': "2022-12-14T21:00:00",
        'date_to': "2022-12-16T10:00:00"
}


    req = get('https://api.hh.ru/vacancies', params) # Посылаем запрос к API
    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    c = json.loads(data)
    return render(request, 'vacancy.html', c)
