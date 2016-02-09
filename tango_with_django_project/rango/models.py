from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    #Exercise 6.9
    views = models.IntegerField(default=0, unique=False)
    likes = models.IntegerField(default=0, unique=False)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0, unique=False)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title