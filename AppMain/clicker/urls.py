from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SumView, clicker

app_name = 'clicker'

urlpatterns = [
    path('', clicker),
    path('api/v2/sum/', SumView.as_view()),
]
