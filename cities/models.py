from django.db import models
from numpy import true_divide

# Create your models here.

class Search(models.Model):
    term = models.CharField(max_length=1000)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)

    class Meta:
        verbose_name_plural = "Searchengine"
    def __str__(self):
        return self.term

#        
class Analytics(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term
#
class Anthropometry(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term
#
class Computer(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term
#
class Distribution(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term


#
class Human(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term

#
class Management(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term
#
class Manufacturing(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term

class new_Operations(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term

class Quality(models.Model):
    term = models.CharField(max_length=200)
    meaning = models.TextField()
    href = models.URLField(max_length=1000,null=True)
    firstkeyword = models.CharField(max_length=200,null=True)
    secondkeyword = models.CharField(max_length=200,null=True)
    lastkeyword = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.term