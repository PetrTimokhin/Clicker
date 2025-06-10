# от Матвея
from loguru import logger
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .models import ModelForClick
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


# мой кликер без API
def clicker(request):
    if request.method == "POST":
        qty_clicks = request.POST['value']

        # ClickCounter.objects.create(clicks=qty_clicks)

        user = request.user.click_counter
        user.clicks = qty_clicks
        user.save()

    user = request.user.click_counter
    clicks = user.clicks
    content = {
        'clicks': int(clicks),
    }
    return render(request, 'clicker/clicker.html', content)


# от Матвея Сумма двух чисел
class SumView(APIView):

    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        try:
            a = float(request.query_params.get('number1'))
            b = float(request.query_params.get('number2'))
        except (TypeError, ValueError):
            return Response(
                {'message': 'Вы ввели не все числа!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        result = a + b

        return Response(
            {'message': str(result)},
            status=status.HTTP_200_OK
        )
