from django.db import models

class Ability(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Move(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    power = models.IntegerField(null=True)
    pp = models.IntegerField(null=True)
    accuracy = models.IntegerField(null=True)
   
    def __str__(self):
        return self.name
    
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)
    held_item = models.TextField(null=True)
    hp = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    special_attack = models.IntegerField(null=True)
    special_defense = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    abilities = models.ManyToManyField(Ability)
    sprites = models.URLField()
    moves = models.ManyToManyField(Move)

    def __str__(self):
        return self.name

