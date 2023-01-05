from art.models import Vacancy
from django.shortcuts import render, redirect


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
    vac = Vacancy.objects.all()
    c = {
        'vc': vac
    }
    return render(request, 'vacancy.html', c)
