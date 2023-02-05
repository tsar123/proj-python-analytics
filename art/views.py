import json
import re
from _datetime import datetime

import requests
from django.shortcuts import render

from art.models import *


def main(request):
    return render(request, 'main.html')


def demand(request):
    lev = LevelSalary.objects.all()
    cou = CountVacancies.objects.all()
    d = {
        'le': lev,
        'co': cou
    }
    return render(request, 'demand.html', d)


def geography(request):
    geo = Geography.objects.all()
    vac = VacancyRate.objects.all()
    c = {
        'ge': geo,
        'va': vac
    }
    return render(request, 'geography.html', c)


def skills(request):
    return render(request, 'skills.html')


def vacancy(request):
    def makeDate(args):
        return str(datetime.strptime(args, '%Y-%m-%dT%H:%M:%S%z').strftime('%d.%m.%Y'))

    def removeTags(args):
        return " ".join(re.sub(r"\<[^>]*\>", "", args).split())

    def makeZ(args):
        res = []
        for i in args:
            for j in i.values():
                res.append(j)
        return ', '.join([g for g in res])

    params = {
        'text': 'NAME:DevOps',
        'page': 0,
        'per_page': 8,
        'only_with_salary': True,
        #'currency': 'RUR',
        'date_from': "2023-02-01T21:00:00",
        'date_to': "2023-02-03T10:00:00"
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    c = json.loads(data)
    n = []
    for g in c['items']:
        rec = requests.get(g['url'])
        data = rec.content.decode()
        rec.close()
        a = json.loads(data)
        a['description'] = removeTags(a['description'])
        a['key_skills'] = makeZ(a['key_skills'])
        a['published_at'] = makeDate(a['published_at'])
        n.append(a)
    ab = {
        'items': n,
    }
    return render(request, 'vacancy.html', ab)
