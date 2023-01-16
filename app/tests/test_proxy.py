from django.core.handlers.wsgi import WSGIRequest
from io import StringIO

from ..proxy import make_absolute_location, get_headers, proxy_response, make_proxy_request


class TestMakeAbsoluteLocation:
    def test_already_absolute(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            'https://example2.com/next/test/path?with=qs')
        assert absurl == 'https://example2.com/next/test/path?with=qs'

    def test_scheme_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            '//example2.com/next/test/path?with=qs')
        assert absurl == 'https://example2.com/next/test/path?with=qs'

    def test_host_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            '/next/test/path?with=qs')
        assert absurl == 'https://example.com/next/test/path?with=qs'

    def test_path_relative(self):
        absurl = make_absolute_location(
            'https://example.com/test/path',
            'next/test/path?with=qs')
        assert absurl == 'https://example.com/test/next/test/path?with=qs'


class TestMakeProxyRequest:
    def test_success(self, mocker):
        request = WSGIRequest({
                'REQUEST_METHOD': 'GET',
                'PATH_INFO': "/",
                'wsgi.input': StringIO(),
                'content-length': 1092,
                'content-encoding': 'utf-8',
                'http_referrer': 'a.com',
        })

        requests_request = mocker.patch("app.proxy.requests.request")
        remote_url = "https://blackrussia.online/"
        make_proxy_request(request, remote_url)

        assert requests_request.call_count == 1
        assert "GET", remote_url == requests_request.call_args[0]


class TestProxyResponse:
    def test_success(self, fake_response):
        response_url = 'https://example.com/test/path'
        location = 'https://example2.com/next/test/path?with=qs'

        fake_response.url = response_url
        fake_response.headers = {
            'location': location,
            'content-length': 1092,
            'content-encoding': 'utf-8',
            'http_referrer': 'a.com',
        }

        response = proxy_response(fake_response)
        assert response['location'] == make_absolute_location(response_url, location)
        assert "http_referrer" in response
        assert "content-length" not in response
        assert "content-encoding" not in response


class TestGetHeaders:
    def test_success(self):
        environ = {
            "HTTP_REFERRER": "https://a.com",
            "SOME_OTHER_HEADER": "OMG",
            "CONTENT_TYPE": "img/png",
        }

        headers = get_headers(environ)
        assert headers["REFERRER"] == environ["HTTP_REFERRER"]
        assert headers["CONTENT-TYPE"] == environ["CONTENT_TYPE"]

        assert "SOME_OTHER_HEADER" not in headers
