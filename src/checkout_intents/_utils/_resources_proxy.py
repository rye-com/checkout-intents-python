from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `checkout_intents.resources` module.

    This is used so that we can lazily import `checkout_intents.resources` only when
    needed *and* so that users can just import `checkout_intents` and reference `checkout_intents.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("checkout_intents.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
