import json

from pathlib import Path
from typing import Dict, Optional, Union

from ..config import DEFAULTS

class BaseRequest:
    """Assertio Request object."""

    def __init__(self, method: Optional[str] = None):
        """Class constructor."""
        self._body: Union[Dict, None] = None
        self._endpoint: Union[str, None] = None
        self._headers: Union[Dict, None] = None
        self._method: Union[str, None] = method
        self._params: Union[Dict, None] = None

    @property
    def body(self):
        """Body getter."""
        return self._body
    
    @body.setter
    def body(self, body: Union[Dict, str]):
        """Body setter."""
        if isinstance(body, str):
            body = Path.cwd().joinpath(f"{DEFAULTS.payloads_dir}/{body}")
        if isinstance(body, Path):
            with open(body) as stream:
                body = json.load(stream)

        self._body = json.dumps(body)

    @property
    def endpoint(self):
        """Endpoint getter, no setter available."""
        return self._endpoint

    @endpoint.setter
    def endpoint(self, new_endpoint):
        """Endpoint setter."""
        self._endpoint = new_endpoint

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
        """Method getter."""
        return self._method

    @method.setter
    def method(self, new_method):
        """Method setter."""
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