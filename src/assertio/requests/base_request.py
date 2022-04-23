import json

from pathlib import Path
from typing import Dict, Optional, List, Union

from pydash import _

from ..bootstrap import _CLI
from ..types import Cookies, Headers, RequestProperty


DEFAULTS = _CLI().get_config()

class BaseRequest:
    """Assertio Request object."""

    def __init__(self, method: Optional[str] = None):
        """Class constructor."""
        self._body: RequestProperty = None
        self._cookies: RequestProperty = None
        self._endpoint: RequestProperty = None
        self._headers: RequestProperty = None
        self._method: RequestProperty = method
        self._params: RequestProperty = None

    @property
    def body(self):
        """Body getter."""
        if isinstance(self._body, str):
            return json.loads(self._body)
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
    def cookies(self):
        """Cookies getter."""
        return self._cookies
    
    @cookies.setter
    def cookies(self, new_cookies: Cookies):
        """Cookies setter."""
        if isinstance(new_cookies, tuple):
            new_cookies = dict(new_cookies)

        if self._cookies is None:
            self._cookies = new_cookies
        else:
            self._cookies.update(new_cookies)

    @property
    def endpoint(self):
        """Endpoint getter, no setter available."""
        return self._endpoint

    @endpoint.setter
    def endpoint(self, new_endpoint: str):
        """Endpoint setter."""
        self._endpoint = new_endpoint

    @property
    def headers(self):
        """Headers getter."""
        return self._headers
    
    @headers.setter
    def headers(self, new_headers: Headers):
        """Headers setter."""
        if isinstance(new_headers, tuple):
            new_headers = dict(new_headers)

        if self._headers is None:
            self._headers = new_headers
        else:
            self._headers.update(new_headers)

    @property
    def method(self):
        """Method getter."""
        return self._method

    @method.setter
    def method(self, new_method: str):
        """Method setter."""
        self._method = new_method

    @property
    def params(self):
        """Query Params getter."""
        return self._params
    
    @params.setter
    def params(self, new_params: Dict):
        """Query Params setter."""
        if self._params is None:
            self._params = new_params
        else:
            self._params.update(new_params)

    def get_response_field(self, path: Union[List[str], str]):
        """Return value from response payload.
        Must be used after perform()
        
        """
        return _.get(self.response.json(), path)