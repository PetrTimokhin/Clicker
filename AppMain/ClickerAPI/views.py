from rest_framework.views import APIView
from rest_framework.response import Response

from ClickerAPI.models import ClickCount
from AppMain.logs.log import logger


# кликер через API
class ClickerView(APIView):
    @logger.catch
    def get(self, request):  # название не менять, это обработчик get запросов
        ip = get_client_ip(request)
        user = ClickCount.objects.filter(ip=ip).first()
        if not user:
            user = ClickCount.objects.create(ip=ip, clicks=0)
        clicks = user.clicks
        logger.error(f'IP: {ip};'
                     f' метод get; '
                     f'Передаваемый параметр: {clicks}; '
                     )
        return Response({'message': str(clicks)})

    @logger.catch
    def post(self, request):  # название post - обработчик post запросов
        # данные не принимаем! просто обрабатываем пустой post, нажатие кнопки.

        # получаем ip
        ip = get_client_ip(request)
        #  Увеличиваем счет пользователя.
        user = ClickCount.objects.filter(ip=ip).first()
        user.clicks += 1
        user.save()
        logger.info(f'IP: {ip}; метод post;')
        return Response({'message': str(user.clicks)})

# как получить ip, первый способ
@logger.catch
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        logger.info(f'IP: {ip}; forwarded_for')
    else:
        ip = request.META.get('REMOTE_ADDR')
        logger.info(f'IP: {ip}; REMOTE_ADDR')
    return ip

# # как получить ip, второй способ
# pip install django-ipware
# from ipware import get_client_ip
#
# def get(request):
#   ip, is_routable = get_client_ip(request)


# API для просмотра ошибок в файле debug.log
class LogsView(APIView):
    def get(self, request):
        dct_log = {}
        n = 0
        with open('AppMain/logs/debug.log', 'r', encoding="utf8") as file:
            for i in file:
                if 'ERROR' in i.split():
                    n += 1
                    dct_log[f'Ошибка {n}'] = i

        return Response({'message': dct_log})


