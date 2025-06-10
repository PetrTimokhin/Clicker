from django.db import models
from django.contrib.auth.models import User


class ModelForClick(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='click_counter')
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f"Пользователь: {self.user.username} , Кликов: {self.clicks};"


