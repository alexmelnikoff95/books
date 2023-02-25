from django.db import models
from django.urls import reverse


class Artist(models.Model):
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилия', max_length=255)
<<<<<<< HEAD
    role = models.CharField('роль', max_length=255, blank=True)
    data_birth = models.DateField('дата рождения', blank=True, default='2000-11-11')

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'
=======
>>>>>>> parent of 01903ff (task_2 Создание и написание миграции.)

    def __str__(self):
        return self.last_name, self.first_name


class Band(models.Model):
    name = models.CharField('название группы', max_length=255)
    artist = models.ManyToManyField(Artist, verbose_name='музыкант')

    def __str__(self):
        return self.name
