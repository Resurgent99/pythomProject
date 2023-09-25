from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models import FloatField
from django.db.models.functions import Cast


class View(models.Model):
    user=models.CharField('Пользователь', max_length=50)
    title=models.CharField('Просмотр', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'



class Product2(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField('Продукт', max_length=50)

    class Meta:
        managed = True
        db_table = 'product2'


class Yrok2(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Название', max_length=50)
    video_name = models.CharField('Ссылка на видео', max_length=50)
    view = models.FloatField('Длительность просмотра', max_length=50)
    slug = models.SlugField(default=' ', null=False, db_index=True)
    location_id = models.ForeignKey(Product2, on_delete=models.CASCADE, null=True)
    data_field = models.DateField()


    class Meta:
        managed = True
        db_table = 'yrok2'

