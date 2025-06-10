from django.db import models
from django.contrib.auth.models import User


class Stuff(models.Model):
    stuff_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.stuff_name


class ClickCount(models.Model):
    stuff_status = models.ForeignKey(to=Stuff, on_delete=models.CASCADE,
                             related_name='clicker_user')  # default ???
    ip = models.GenericIPAddressField(unique=True, default=0)
    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Пользователь IP: {self.ip} , Кликов: {self.clicks};"
