from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description_short = models.CharField('Краткое описание', max_length=250)
    description_long = HTMLField('Описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE)
    url = models.ImageField('Фото')
    position = models.IntegerField('Позиция')

    def __str__(self):
        return f'{self.position} {self.place.title}'

    class Meta:
        ordering = 'position',