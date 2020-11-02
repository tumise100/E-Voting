from django.contrib.auth.models import AbstractUser
import datetime
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.utils import timezone



class Polls(models.Model):
    choice = [('DEPT', 'Departmental Election'),
              ('FACE','Faculty Election'),
              ('SUG', 'Student Union Government Election')]
    Type = models.CharField(max_length=4, choices=choice, verbose_name='Type',
                                   help_text='Designate whether the election is Departmental, Faculty or Sug Election')
    Category = models.CharField(max_length=150, help_text='Designate which department or faculty. If SUG leave blank', blank=True, verbose_name='Dept/Faculty')
    Award = models.CharField(max_length=100, verbose_name='Position')
    pub_date = models.DateField('Date', auto_now=True)
    deadline = models.DateTimeField('Deadline')

    def __str__(self):
        return self.Award


class Choice(models.Model):
    polls = models.ForeignKey(Polls, on_delete=models.CASCADE)
    candidates = models.CharField(max_length=200)
    image = models.ImageField(upload_to="image/", blank=True)
    bio = models.TextField(max_length=100, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.candidates


class User(AbstractUser):
    Matric = models.CharField(max_length=20, blank=False, verbose_name='Matric No.')
    Other_Name = models.CharField(max_length=30)
    email = models.EmailField()
    Faculty = models.CharField(max_length=50)
    Dept = models.CharField(max_length=50, verbose_name='Department')
    Tel = models.CharField(max_length=11)
    is_voter = models.BooleanField(default=False)
    count = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return self.first_name


class VOTED(models.Model):
    has_voted = models.ForeignKey(Polls, on_delete=models.SET_NULL, blank=True, null=True, related_name='voting')
    user_voted = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_voted')
    Voted = models.BooleanField(default=False)

    def __str__(self):
        return "%s the user" (self.user_voted.first_name, self.Voted, self.has_voted.Award)
    @classmethod
    def create(cls, has_voted, user_voted, Voted):
        is_voting = cls(has_voted=has_voted, user_voted=user_voted, Voted=Voted)
        return is_voting

@receiver(pre_save, sender=User)
def slugify_name(sender, instance, *args, **kwargs):
    instance.username = slugify(instance.Matric)