from django.db import models
import pdb

# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=360)
    img = models.ImageField(upload_to='genre_imgs',
                            null=True,
                            blank=True)
    subgenres = models.ManyToManyField(
        'self',
        through='GenreJoin',
        symmetrical=False,
        null=True,
        blank=True,
        related_name='is_topgenre_of')

    def save(self, *args, **kwargs):
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class GenreJoin(models.Model):
    genre = models.ForeignKey(Genre,
                              related_name='genre')
    subgenre = models.ForeignKey(Genre,
                                 related_name='subgenre')
    weight = models.FloatField(default=0)
