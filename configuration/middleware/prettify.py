from bs4 import BeautifulSoup


class PrettifyMiddleware(object):
    """
    Cleans up the HTML for nice pretty indentation and viewing
    """
    def process_response(self, request, response):
        if response.has_header('Content-Type') and response['Content-Type'].startswith('text/html'):
            response.content = BeautifulSoup(response.content).prettify()

        return response
