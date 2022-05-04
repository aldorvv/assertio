"""Types and aliases."""
from typing import Callable, Dict, List, Tuple, Union
from collections import namedtuple

PreconditionParams = Union[Dict[str, str], Tuple[Tuple[str, str], ...]]
Cookies = PreconditionParams
Headers = PreconditionParams

RequestProperty = Union[Union[Dict, None], Union[str, None]]
MethodList =  List[Callable[..., None]]

TestMethod = namedtuple("TestMethod", "function,weight")
TestMethods = List[TestMethod]