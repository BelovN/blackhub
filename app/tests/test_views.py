from django.http import HttpResponse
from django.test import Client


class TestBlackhubView:
    URI = ["/", "/politics.html", "/donate.php"]

    def test_success_calls(self, mocker, fake_response):
        client = Client()

        make_proxy_request = mocker.patch("app.views.make_proxy_request", return_value=fake_response)
        handle_response = mocker.patch("app.views.handle_response", return_value=fake_response)

        fake_proxy_response = HttpResponse(
            fake_response.content,
            status=fake_response.status_code
        )
        proxy_response = mocker.patch("app.views.proxy_response", return_value=fake_proxy_response)

        call_count = 1
        for uri in self.URI:
            response = client.get(uri)

            assert make_proxy_request.call_count == call_count
            assert handle_response.call_count == call_count
            assert proxy_response.call_count == call_count

            call_count += 1

            assert response.status_code == 200

    def test_error(self, mocker):

        def exception_raiser():
            raise ValueError()

        client = Client()
        mocker.patch(
            "app.views.make_proxy_request",
            side_effect=exception_raiser
        )

        for uri in self.URI:
            response = client.get(uri)
            assert response.status_code == 504

