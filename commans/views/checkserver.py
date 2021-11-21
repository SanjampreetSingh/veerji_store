from rest_framework.decorators import api_view
from datetime import datetime
from utils.response_utils import ResponseUtils as res


@api_view(['GET'])
def checkserver(request):
    message = 'Server is live at ' +\
        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return res.respond_success(details=message)
