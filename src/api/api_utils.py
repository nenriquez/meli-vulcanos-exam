import functools

from webapp2 import exc


def get_int_from_param(param):
    try:
        i = int(param)
    except Exception as err:
        raise exc.HTTPBadRequest(detail=str(err))
    return i


def require_params(names):
    """
    This decorator validates if all parameters are present in the request.
    """
    def method_wrap(method):
        @functools.wraps(method)
        def wrap(self, *args, **kwds):
            for name in names:
                params = self.request.params.items()
                keys = [item[0] for item in params]
                if name not in keys:
                    raise exc.HTTPBadRequest("{} argument missing.".format(name))
            return method(self, *args, **kwds)
        return wrap
    return method_wrap


def _set_default_headers(self):
    origin = '*'
    self.response.headers["Access-Control-Allow-Origin"] = origin
    self.response.headers['Content-Type'] = 'application/json'


def with_default_headers():
    """
    This decorator will add mandatory headers to serve secure responses.
    """
    def method_wrap(method):
        @functools.wraps(method)
        def wrap(self, *args, **kwds):
            _set_default_headers(self)
            return method(self, *args, **kwds)
        return wrap
    return method_wrap


def with_coors_headers():
    """
    This decorator will add mandatory headers to serve secure responses.
    """
    def method_wrap(method):
        @functools.wraps(method)
        def wrap(self, *args, **kwds):

            _set_default_headers(self)

            self.response.headers.add_header("Access-Control-Allow-Credentials", "true")
            self.response.headers.add_header("Access-Control-Allow-Headers", "Origin, Content-Type")
            self.response.headers.add_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
            self.response.headers.add_header("Access-Control-Max-Age", "86400")

            return method(self, *args, **kwds)
        return wrap
    return method_wrap
