from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.CharField('Статья', max_length=1000)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
