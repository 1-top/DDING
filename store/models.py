from django.db import models


class Report(models.Model):
    latitude = models.CharField(max_length=32, verbose_name='위도')
    longitude = models.CharField(max_length=32, verbose_name='경도')
    location = models.CharField(max_length=128, verbose_name='위치')
    name = models.CharField(max_length=32, verbose_name='가게이름')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='카테고리')

    class Meta:
        verbose_name = '제보'
        verbose_name_plural = '제보'


class Category(models.Model):
    name = models.CharField(max_length=16, verbose_name='카테고리종류')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = '카테고리'


class Store(models.Model):
    latitude = models.CharField(max_length=32, verbose_name='위도')
    longitude = models.CharField(max_length=32, verbose_name='경도')
    location = models.CharField(max_length=128, verbose_name='위치')
    name = models.CharField(max_length=32, verbose_name='가게이름')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '가게'
        verbose_name_plural = '가게'
