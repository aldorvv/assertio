from typing import Dict, Union


class BaseRequest:
    """Assertio Request object."""

    def __init__(self):
        """Class constructor."""
        self._body: Union[Dict, None] = None
        self._endpoint: Union[str, None] = None
        self._headers: Union[Dict, None] = None
        self._method: Union[str, None] = None
        self._params: Union[Dict, None] = None

    @property
    def body(self):
        """Body getter."""
        return self._body
    
    @body.setter
    def body(self, new_body):
        """Body setter."""
        if self._body is None:
            self._body = new_body
        else:
            self._body.update(new_body)

    @property
    def endpoint(self):
        """Endpoint getter, no setter available."""
        return self._endpoint

    @property
    def headers(self):
        """Headers getter."""
        return self._headers
    
    @headers.setter
    def headers(self, new_headers):
        """Headers setter."""
        if self._headers is None:
            self._headers = new_headers
        else:
            self._headers.update(new_headers)

    @property
    def method(self):
        return self._method
    
    @method.setter
    def method(self, new_method):
        self._method = new_method

    @property
    def params(self):
        return self._params
    
    @params.setter
    def params(self, new_params):
        if self._params is None:
            self._params = new_params
        else:
            self._params.update(new_params)