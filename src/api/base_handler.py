import logging

import webapp2

from api.api_utils import with_coors_headers

_ERROR_MSG_FORMAT = "[Request: %s %s]\r"

class BaseRequestHandler(webapp2.RequestHandler):

    def handle_exception(self, exception, debug):
        self.response.headers['Content-Type'] = 'application/json'
        if issubclass(type(exception), webapp2.exc.HTTPError):
            self.response.status = "{0} {1}".format(exception.code, exception.title)
        else:
            self.response.status = '500 Internal Server Error'

        msg = _ERROR_MSG_FORMAT % (self.request.method, self.request.url)

        logging.exception(msg)
        self.response.out.write(exception)

    @with_coors_headers()
    def head(self, *args, **kwargs):
        self.response.set_status(200)
        self.response.out.write("")

    @with_coors_headers()
    def options(self, *args, **kwargs):
        self.response.set_status(200)
        self.response.out.write("")