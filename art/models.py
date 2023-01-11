from django.db import models


class Vacancy(models.Model):
    name = models.CharField(max_length=1000)
    descriptions = models.CharField(max_length=1000)
    key_skills = models.CharField(max_length=1000)
    department = models.CharField(max_length=1000)
    salary_from = models.CharField(max_length=1000)
    salary_to = models.CharField(max_length=1000)
    area_name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=1000)


class Geography(models.Model):
    city = models.CharField(max_length=40)
    level = models.CharField(max_length=10)


class VacancyRate(models.Model):
    city = models.CharField(max_length=40)
    rate = models.CharField(max_length=10)

class LevelSalary(models.Model):
    year = models.CharField(max_length=10)
    averageSalary = models.CharField(max_length=10)
    salaryDevops = models.CharField(max_length=10)

class CountVacancies(models.Model):
    year = models.CharField(max_length=10)
    countVacancies = models.CharField(max_length=10)
    vacanciesDevops = models.CharField(max_length=10)
