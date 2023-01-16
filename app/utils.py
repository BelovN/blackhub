from requests import Response


def handle_response(response: Response) -> None:
    """Update redirect host in script and change company name"""

    if "html" in response.headers["Content-Type"]:

        # change host in antiddos script
        response._content = response.text.replace(
            "https://blackrussia.online:443/",
            "http://localhost:8000/",
        )
        response._content = response._content.replace(
            "BLACK RUSSIA", "BLACK HUB GAMES"
        )
