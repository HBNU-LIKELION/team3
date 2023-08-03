from django.db import models

class Info(models.Model): #models 안에 있는 Model 클래스를 상속받는 것.
    target = models.TextField(verbose_name="target", null=True, blank='Ture')
    title = models.TextField(verbose_name="title")
    place = models.TextField(verbose_name="place")
    date = models.TextField(verbose_name="date")
    url = models.TextField(verbose_name="urls")