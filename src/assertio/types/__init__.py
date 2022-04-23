"""Types and aliases."""
from typing import Callable, Dict, List, Tuple, Union

PreconditionParams = Union[Dict[str, str], Tuple[Tuple[str, str], ...]]
Cookies = PreconditionParams
Headers = PreconditionParams

RequestProperty = Union[Union[Dict, None], Union[str, None]]
MethodsList =  List[Callable[..., None]]
