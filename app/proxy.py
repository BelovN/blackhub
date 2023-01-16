import re
import logging
from urllib.parse import urlparse

import requests
from requests import Request, Response
from django.http import HttpResponse, QueryDict
from django.core.handlers.wsgi import WSGIRequest

logger = logging.getLogger("django")


def make_proxy_request(request: WSGIRequest, url: str) -> Request:
    """
    Setup by client headers and 
    make proxy request for remote uri
    """

    requests_args = {}
    headers = get_headers(request.META)
    params = request.GET.copy()

    if 'headers' not in requests_args:
        requests_args['headers'] = {}
    if 'data' not in requests_args:
        requests_args['data'] = request.body
    if 'params' not in requests_args:
        requests_args['params'] = QueryDict('', mutable=True)

    headers.update(requests_args['headers'])
    params.update(requests_args['params'])

    for key in list(headers.keys()):
        if key.lower() == 'content-length':
            del headers[key]

    requests_args['headers'] = headers
    requests_args['params'] = params

    try:
        response = requests.request(request.method, url, **requests_args)
    except Exception as e:
        logger.error("Bad proxy request.", exc_info=True)
        raise e

    logger.info("Proxy request", extra={"url": url, "response_status": response.status_code})

    return response


def proxy_response(response: Response) -> HttpResponse:
    """Remove hop-by-hop headers"""

    proxy_response = HttpResponse(
        response.content,
        status=response.status_code)

    excluded_headers = set([
        'connection', 'keep-alive', 'proxy-authenticate',
        'proxy-authorization', 'te', 'trailers', 'transfer-encoding',
        'upgrade',
        'content-encoding',
        'content-length',
    ])
    for key, value in response.headers.items():
        if key.lower() in excluded_headers:
            continue
        elif key.lower() == 'location':
            proxy_response[key] = make_absolute_location(response.url, value)
        else:
            proxy_response[key] = value

    return proxy_response


def make_absolute_location(base_url: str, location: str) -> str:

    absolute_pattern = re.compile(r'^[a-zA-Z]+://.*$')
    if absolute_pattern.match(location):
        return location

    parsed_url = urlparse(base_url)

    if location.startswith('//'):
        return parsed_url.scheme + ':' + location

    elif location.startswith('/'):
        return parsed_url.scheme + '://' + parsed_url.netloc + location

    else:
        return (
            parsed_url.scheme +
            '://' +
            parsed_url.netloc +
            parsed_url.path.rsplit('/', 1)[0] +
            '/' + location
        )


def get_headers(environ: dict) -> dict:
    """Correction headers for proxy query"""

    headers = {}
    for key, value in environ.items():
        if key.startswith('HTTP_') and key != 'HTTP_HOST':
            headers[key[5:].replace('_', '-')] = value
        elif key in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            headers[key.replace('_', '-')] = value

    return headers
