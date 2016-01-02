from __future__ import unicode_literals
import datetime
from django.db import models

class Movie(models.Model):
    LANGUAGE_CHOICES = (
        ('telugu', 'Telugu'),
        ('hindi', 'Hindi'),
        ('tamil', 'Tamil'),
        ('kannada', 'Kannada'),
        ('malayalam', 'Malayalam'),
        ('marathi', 'Marathi'),
    )

    YEAR_CHOICES = []
    for r in reversed(range(1913, (datetime.datetime.now().year+5))):
        YEAR_CHOICES.append((r,r))

    title = models.CharField(max_length=40)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, blank=True, null=True)
    playtime = models.PositiveSmallIntegerField(blank=True, null=True)
    tagline = models.CharField(max_length=140, blank=True, null=True)
    language = models.CharField(default='telugu',
                    choices=tuple(sorted(LANGUAGE_CHOICES, key=lambda item: item[1])),
                    max_length=20)
    # poster = models.ImageField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'year')

    def __unicode__(self):
        return self.title+" ("+str(self.year)+")"

class Artist(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    EYE_COLOR_CHOICES = (
        ('black', 'Black'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    eye_color = models.CharField(choices=EYE_COLOR_CHOICES, max_length=20, blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    # display_pic = models.ImageField(blank=True, null=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name

class MovieCrew(models.Model):
    ROLE_CHOICES = (
        ('actor', 'Actor'),
        ('director', 'Director'),
        ('music_director', 'Music Director'),
        ('singer', 'Singer'),
        ('producer', 'Producer'),
    )

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    character_name = models.CharField(max_length=140, blank=True)

    class Meta:
        unique_together = ('movie', 'artist', 'role', 'character_name')
