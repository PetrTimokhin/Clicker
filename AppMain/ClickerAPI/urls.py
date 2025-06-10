from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import ClickerView, LogsView

app_name = 'ClickerAPI'

urlpatterns = [
    path('clicks/', ClickerView.as_view()),
    path('logs/', LogsView.as_view()),
]
