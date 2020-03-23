from django.db import models

class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60, unique=True)
    emailAddress = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class module(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        unique_together = ('code', 'year', 'semester')

class professor(models.Model):
    id = models.AutoField(primary_key=True)
    pro_id = models.CharField(unique=True, max_length=60)
    name = models.CharField(unique=True, max_length=60)

class relation(models.Model):
    id = models.AutoField(primary_key=True)
    mod = models.ForeignKey('module', on_delete=models.CASCADE)
    pro = models.ForeignKey('professor', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mod', 'pro')

class user_rating(models.Model):
    relation = models.ForeignKey('relation', on_delete=models.CASCADE)
    rate = models.IntegerField()

