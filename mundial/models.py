from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

RESULTS_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('X', 0),
)

class MyAccountManager(BaseUserManager):

    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("Users must have an username.")
        if not password:
            raise ValueError("Users must have a password.")
        user = self.model(
            username=username,
            **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password):
        return self._create_user(username, password)
    def create_superuser(self, username, password, **kwargs):
        user = self.create_user(
            username=username,
            password=password,
            **kwargs
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    points = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def is_admin(self, obj=None):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

class Match(models.Model):
    home_team = models.CharField(max_length=20)
    away_team = models.CharField(max_length=20)
    date = models.DateField()
    result = models.CharField(max_length=1, choices=RESULTS_CHOICES, default='', null=False)
    score = models.CharField(max_length=3, default=0)

class Bet(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    author = models.CharField(max_length=30)
    bet_result = models.CharField(max_length=1, choices=RESULTS_CHOICES, default='', null=False)
    bet_score = models.CharField(max_length=3, default=0)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish_bet(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.value