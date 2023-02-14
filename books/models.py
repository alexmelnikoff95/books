from django.db import models


# Create your models here.
class Artist(models.Model):
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилия', max_length=255)

    def __str__(self):
        return self.last_name, self.first_name


class Band(models.Model):
    name = models.CharField('название группы', max_length=255)
    artist = models.ManyToManyField(Artist, verbose_name='музыкант')

    def __str__(self):
        return self.name
