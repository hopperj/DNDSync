from django.db import models
from django.db.models import permalink
from django.conf import settings
from django.conf import settings as django_settings
from django.db import models


class Mods(models.Model):
    name=models.CharField(max_length=30)
    value=models.IntegerField()

class JournalEntries(models.Model):
    date=models.DateTimeField( auto_now_add=True)
    value=models.TextField(max_length=255, default="", unique=False, blank=True)
    
class Notes(models.Model):
    date=models.DateTimeField( auto_now_add=True)
    value=models.TextField(max_length=255, default="", unique=False, blank=True)


    
class Character(models.Model):

    charName=models.CharField(max_length=30)
    campaignName=models.CharField(max_length=30, unique=False, blank=True)

    notes=models.ForeignKey(Notes, blank=True, null=True)
    journal=models.ForeignKey(JournalEntries, blank=True, null=True)


    maxHP=models.IntegerField(default=0)
    currentHP=models.IntegerField(default=0)
    currentTempHP=models.IntegerField(default=0)

    totalSurges=models.IntegerField(default=0)
    currentSurges=models.IntegerField(default=0)

    totalHP=models.IntegerField(default=0)
    currentHP=models.IntegerField(default=0)


    currentActionPoints=models.IntegerField(default=0)


    abilityMods = models.ForeignKey(Mods, blank=True, null=True)

    ac=models.IntegerField(default=0)
    fort=models.IntegerField(default=0)
    ref=models.IntegerField(default=0)
    will=models.IntegerField(default=0)



    
