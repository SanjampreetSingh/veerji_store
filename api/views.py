from utils.response_utils import ResponseUtils as res
from datetime import datetime
from rest_framework.decorators import api_view
from django.http import JsonResponse


def home(request):
    return JsonResponse({'info': 'Django React Course'})


@api_view(['GET'])
def checkserver(request):
    message = 'Server is live at ' +\
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return res.respond_success(details=message)
