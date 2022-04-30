from django.db import models

genres = (
    ('action', 'action'),
    ('adventure', 'adventure'),
    ('comedy', 'comedy'),
    ('crime', 'crime'),
    ('drama', 'drama'),
    ('musical', 'musical'),
    ('horror', 'horror'),
    ('sci-fi', 'sci-fi'),
    ('thriller', 'thriller'),
)


class Movie(models.Model):
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    genre = models.CharField(max_length=10, choices=genres, default='n/a')
    release_year = models.PositiveIntegerField(null=False, default=2022)

    def __str__(self):
        return self.name