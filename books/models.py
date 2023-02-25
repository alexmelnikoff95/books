from django.db import models
from django.urls import reverse


class Artist(models.Model):
    first_name = models.CharField('имя', max_length=255)
    last_name = models.CharField('фамилия', max_length=255)
    role = models.CharField('роль', max_length=255, blank=True)
    data_birth = models.DateField('дата рождения', blank=True, default='2000-11-11')

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = 'Артисты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Band(models.Model):
    name = models.CharField('название группы', max_length=255)
    artist = models.ManyToManyField(Artist, verbose_name='музыкант')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
