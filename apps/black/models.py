# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import *
from django.db import models

# Create your models here.


class Poke(models.Model):
    poker = models.ForeignKey(User, related_name="pokerpokes")
    poked = models.ForeignKey(User, related_name="pokedpokes")
    created_at = models.DateField(null=True)
    counter = models.IntegerField(blank=False, default=0, null=True)
    total = models.IntegerField(blank=False, default=0, null=True)
