from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MasterUser(models.User):
    name = models.CharField(max_length=128, unique=True)
    alt_email = models.EmailField()
    dob = models.CharField()
    gender = models.CharField()
    profession = models.CharField()
    address = models.TextField()
    mobile = models.IntegerField()
    landline = models.IntegerField()
    city = models.CharField()
    state = models.CharField()
    country = models.CharField()
    nationality = models.CharField()
    language = models.CharField()

    def __unicode__(self):
      return self.name


class Sharer(models.MasterUser):
    user = models.OneToOneField(MasterUser)

    def __unicode__(self):
      return self.user


class Getter(models.MasterUser):
    user = models.OneToOneField(User)

    def __unicode__(self):
      return self.user


class Notification(models.Model):
    status = models.CharField()
    sender = models.CharField()
    receiver = models.CharField()

    def __unicode__(self):
        return self.status
