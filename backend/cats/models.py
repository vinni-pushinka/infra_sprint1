from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Achievement(models.Model):
    '''Класс для представления достижения кота.'''
    name = models.CharField(
        max_length=64, verbose_name='Достижение')

    def __str__(self):
        return self.name


class Cat(models.Model):
    '''Класс для представления кота.'''
    name = models.CharField(max_length=16, verbose_name='Имя')
    color = models.CharField(max_length=16, verbose_name='Окрас')
    birth_year = models.IntegerField(verbose_name='Год рождения')
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
        )
    achievements = models.ManyToManyField(
        Achievement, through='AchievementCat')
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None,
        )

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    '''Класс для связи между котом и достижением.'''
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
