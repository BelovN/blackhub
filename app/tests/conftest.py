import pytest
from requests import Response


@pytest.fixture
def fake_response():
    response = Response()
    response._content = "Some Fake Content"
    response.status_code = "200"

    return response 


@pytest.fixture
def html_response(fake_response):
    fake_response.headers["Content-Type"] = "text/html"
    return fake_response


@pytest.fixture
def png_response(fake_response):
    fake_response.headers["Content-Type"] = "image/png"
    return fake_response