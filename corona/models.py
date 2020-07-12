from django.db import models

class corona(models.Model):
    test = models.IntegerField()
    affected = models.IntegerField()
    recovared = models.IntegerField()
    deth = models.IntegerField()
    total_deth = models.IntegerField()
    total_test = models.IntegerField()
    total_affected = models.IntegerField()
    totel_recovared = models.IntegerField()
    total_deth = models.IntegerField()

class update(models.Model):
    update_news = models.CharField(max_length=500)

class rugi(models.Model):
    name = models.CharField(max_length=150)
    postcode = models.IntegerField()
    number = models.IntegerField()
    problem = models.CharField(max_length=1000)
    password = models.CharField(max_length=400)