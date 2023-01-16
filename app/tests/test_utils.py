from ..utils import handle_response
from .data import BASE_HTML, BASE_SCRIPT


class TestHandleResponse:

    def test_handle_response_script(self, html_response):
        html_response._content = BASE_SCRIPT.encode()
        handle_response(html_response)

        changed_host = BASE_SCRIPT.replace(
            "https://blackrussia.online:443/",
            "http://localhost:8000/",
        )

        assert html_response._content == changed_host


    def test_handle_response_html(self, html_response):
        html_response._content = BASE_HTML.encode()
        handle_response(html_response)

        changed_blackhub = BASE_HTML.replace(
            "BLACK RUSSIA", "BLACK HUB GAMES"
        )
        assert html_response._content == changed_blackhub


    def test_handle_response_not_html(self, png_response):
        content = "BLACK RUSSIA, https://blackrussia.online:443/".encode()
        png_response._content = content
        handle_response(png_response)

        assert png_response._content == content