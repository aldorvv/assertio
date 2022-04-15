from typing import Dict, Union


class BaseRequest:
    """Assertio Request object."""

    def __init__(self):
        """Class constructor."""
        self.body: Union[Dict, None] = None
        self.headers: Union[Dict, None] = None
        self.params: Union[Dict, None] = None
