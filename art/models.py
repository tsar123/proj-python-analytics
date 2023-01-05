from django.db import models

# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=1000)
    descriptions = models.CharField(max_length=1000)
    key_skills = models.CharField(max_length=1000)
    department = models.CharField(max_length=1000)
    salary_from = models.CharField(max_length=1000)
    salary_to = models.CharField(max_length=1000)
    area_name = models.CharField(max_length=1000)
    published_at = models.CharField(max_length=1000)
