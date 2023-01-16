from django.conf import settings
from django.http import HttpResponse
from django.views import View

from .proxy import make_proxy_request, proxy_response
from .utils import handle_response

import logging

logger = logging.getLogger("error")

class BlackhubView(View):

    def get(self, request) -> HttpResponse:
        
        try:
            # build a proxi remote url
            remote_url = settings.PROXY_REMOTE_URL
            if len(request.path) > 1:
                remote_url += request.path

            response = make_proxy_request(request, remote_url)
            
            handle_response(response)

            proxy = proxy_response(response)

            return proxy
        
        except Exception as e:
            logger.error("Bad proxy request " + str(e))
            return HttpResponse(status=504)