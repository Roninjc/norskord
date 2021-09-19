"""modelos con el vocabulario noruego y las características"""
from django.db import models


class Ordforrad(models.Model):
    """classe del vocabulario noruego"""
    word_id = models.AutoField(primary_key=True)
    norwegian = models.CharField(max_length=200, unique=True)
    english = models.CharField(max_length=200)
    WordClass = models.TextChoices('WordClass', 'noun verb adjective')
    word_class = models.CharField(blank=True, choices=WordClass.choices, max_length=20)
    LvlUsage = models.TextChoices('lvl usage', 'high medium low')
    lvl_usage = models.CharField(blank=True, choices=LvlUsage.choices, max_length=20)
    usage_fr = models.IntegerField()
    usage_permll = models.FloatField()

class NounsFeatures(models.Model):
    """clase de las características de los sustantivos"""
    noun_id = models.AutoField(primary_key=True)
    norwegian = models.OneToOneField(
        Ordforrad,
        on_delete=models.CASCADE
    )
    gender = models.TextChoices('gender', 'masculine feminine neutrum')
    plural = models.BooleanField("used in plural")
    mass_noun = models.BooleanField()

class VerbsFeatures(models.Model):
    """clase de las características de los verbos"""
    verb_id = models.AutoField(primary_key=True)
    norwegian = models.OneToOneField(
        Ordforrad,
        on_delete=models.CASCADE,
    )
    valency = models.IntegerField()
    transitivity = models.TextChoices(
        'transitivity', 'alternating transitive intransitive ditransitive'
        )
    multi_world = models.BooleanField("multi world phrase")
    