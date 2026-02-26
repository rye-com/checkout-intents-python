# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, CheckoutIntentsError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import betas, brands, products, checkout_intents
    from .resources.brands import BrandsResource, AsyncBrandsResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.betas.betas import BetasResource, AsyncBetasResource
    from .resources.checkout_intents import CheckoutIntentsResource, AsyncCheckoutIntentsResource

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "CheckoutIntents",
    "AsyncCheckoutIntents",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "staging": "https://staging.api.rye.com/",
    "production": "https://api.rye.com/",
}


def _extract_environment_from_api_key(api_key: str) -> Literal["staging", "production"] | None:
    """
    Extracts the environment from a Rye API key.
    API keys follow the format: RYE/{environment}-{key}

    Args:
        api_key: The API key to parse

    Returns:
        The extracted environment ('staging' or 'production'), or None if the format doesn't match
    """
    import re

    match = re.match(r"^RYE/(staging|production)-", api_key)
    return match.group(1) if match else None  # type: ignore[return-value]


class CheckoutIntents(SyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["staging", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["staging", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous CheckoutIntents client instance.

        This automatically infers the `api_key` argument from the `CHECKOUT_INTENTS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CHECKOUT_INTENTS_API_KEY")
        if api_key is None:
            raise CheckoutIntentsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CHECKOUT_INTENTS_API_KEY environment variable"
            )
        self.api_key = api_key

        # Auto-infer environment from API key
        inferred_environment = _extract_environment_from_api_key(api_key)

        # Validate environment option matches API key (if both provided)
        if is_given(environment) and inferred_environment and environment != inferred_environment:
            raise CheckoutIntentsError(
                f"Environment mismatch: API key is for '{inferred_environment}' environment but 'environment' option is set to '{environment}'. Please use an API key that matches your desired environment or omit the 'environment' option to auto-detect from the API key (only auto-detectable with the RYE/{{environment}}-abcdef api key format)."
            )

        # Use provided environment, or infer from API key, or default to staging
        resolved_environment: Literal["staging", "production"]
        if is_given(environment):
            resolved_environment = cast(Literal["staging", "production"], environment)
            self._environment = cast(Literal["staging", "production"], environment)
        elif inferred_environment:
            resolved_environment = inferred_environment
            self._environment = inferred_environment
        else:
            resolved_environment = "staging"
            self._environment = "staging"

        base_url_env = os.environ.get("CHECKOUT_INTENTS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CHECKOUT_INTENTS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[resolved_environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {resolved_environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            try:
                base_url = ENVIRONMENTS[resolved_environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {resolved_environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def checkout_intents(self) -> CheckoutIntentsResource:
        from .resources.checkout_intents import CheckoutIntentsResource

        return CheckoutIntentsResource(self)

    @cached_property
    def betas(self) -> BetasResource:
        from .resources.betas import BetasResource

        return BetasResource(self)

    @cached_property
    def brands(self) -> BrandsResource:
        from .resources.brands import BrandsResource

        return BrandsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def with_raw_response(self) -> CheckoutIntentsWithRawResponse:
        return CheckoutIntentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutIntentsWithStreamedResponse:
        return CheckoutIntentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["staging", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCheckoutIntents(AsyncAPIClient):
    # client options
    api_key: str

    _environment: Literal["staging", "production"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["staging", "production"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCheckoutIntents client instance.

        This automatically infers the `api_key` argument from the `CHECKOUT_INTENTS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CHECKOUT_INTENTS_API_KEY")
        if api_key is None:
            raise CheckoutIntentsError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CHECKOUT_INTENTS_API_KEY environment variable"
            )
        self.api_key = api_key

        # Auto-infer environment from API key
        inferred_environment = _extract_environment_from_api_key(api_key)

        # Validate environment option matches API key (if both provided)
        if is_given(environment) and inferred_environment and environment != inferred_environment:
            raise CheckoutIntentsError(
                f"Environment mismatch: API key is for '{inferred_environment}' environment but 'environment' option is set to '{environment}'. Please use an API key that matches your desired environment or omit the 'environment' option to auto-detect from the API key (only auto-detectable with the RYE/{{environment}}-abcdef api key format)."
            )

        # Use provided environment, or infer from API key, or default to staging
        resolved_environment: Literal["staging", "production"]
        if is_given(environment):
            resolved_environment = cast(Literal["staging", "production"], environment)
            self._environment = cast(Literal["staging", "production"], environment)
        elif inferred_environment:
            resolved_environment = inferred_environment
            self._environment = inferred_environment
        else:
            resolved_environment = "staging"
            self._environment = "staging"

        base_url_env = os.environ.get("CHECKOUT_INTENTS_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `CHECKOUT_INTENTS_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[resolved_environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {resolved_environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            try:
                base_url = ENVIRONMENTS[resolved_environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {resolved_environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

    @cached_property
    def checkout_intents(self) -> AsyncCheckoutIntentsResource:
        from .resources.checkout_intents import AsyncCheckoutIntentsResource

        return AsyncCheckoutIntentsResource(self)

    @cached_property
    def betas(self) -> AsyncBetasResource:
        from .resources.betas import AsyncBetasResource

        return AsyncBetasResource(self)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        from .resources.brands import AsyncBrandsResource

        return AsyncBrandsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCheckoutIntentsWithRawResponse:
        return AsyncCheckoutIntentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutIntentsWithStreamedResponse:
        return AsyncCheckoutIntentsWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["staging", "production"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CheckoutIntentsWithRawResponse:
    _client: CheckoutIntents

    def __init__(self, client: CheckoutIntents) -> None:
        self._client = client

    @cached_property
    def checkout_intents(self) -> checkout_intents.CheckoutIntentsResourceWithRawResponse:
        from .resources.checkout_intents import CheckoutIntentsResourceWithRawResponse

        return CheckoutIntentsResourceWithRawResponse(self._client.checkout_intents)

    @cached_property
    def betas(self) -> betas.BetasResourceWithRawResponse:
        from .resources.betas import BetasResourceWithRawResponse

        return BetasResourceWithRawResponse(self._client.betas)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithRawResponse:
        from .resources.brands import BrandsResourceWithRawResponse

        return BrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)


class AsyncCheckoutIntentsWithRawResponse:
    _client: AsyncCheckoutIntents

    def __init__(self, client: AsyncCheckoutIntents) -> None:
        self._client = client

    @cached_property
    def checkout_intents(self) -> checkout_intents.AsyncCheckoutIntentsResourceWithRawResponse:
        from .resources.checkout_intents import AsyncCheckoutIntentsResourceWithRawResponse

        return AsyncCheckoutIntentsResourceWithRawResponse(self._client.checkout_intents)

    @cached_property
    def betas(self) -> betas.AsyncBetasResourceWithRawResponse:
        from .resources.betas import AsyncBetasResourceWithRawResponse

        return AsyncBetasResourceWithRawResponse(self._client.betas)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithRawResponse:
        from .resources.brands import AsyncBrandsResourceWithRawResponse

        return AsyncBrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)


class CheckoutIntentsWithStreamedResponse:
    _client: CheckoutIntents

    def __init__(self, client: CheckoutIntents) -> None:
        self._client = client

    @cached_property
    def checkout_intents(self) -> checkout_intents.CheckoutIntentsResourceWithStreamingResponse:
        from .resources.checkout_intents import CheckoutIntentsResourceWithStreamingResponse

        return CheckoutIntentsResourceWithStreamingResponse(self._client.checkout_intents)

    @cached_property
    def betas(self) -> betas.BetasResourceWithStreamingResponse:
        from .resources.betas import BetasResourceWithStreamingResponse

        return BetasResourceWithStreamingResponse(self._client.betas)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithStreamingResponse:
        from .resources.brands import BrandsResourceWithStreamingResponse

        return BrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)


class AsyncCheckoutIntentsWithStreamedResponse:
    _client: AsyncCheckoutIntents

    def __init__(self, client: AsyncCheckoutIntents) -> None:
        self._client = client

    @cached_property
    def checkout_intents(self) -> checkout_intents.AsyncCheckoutIntentsResourceWithStreamingResponse:
        from .resources.checkout_intents import AsyncCheckoutIntentsResourceWithStreamingResponse

        return AsyncCheckoutIntentsResourceWithStreamingResponse(self._client.checkout_intents)

    @cached_property
    def betas(self) -> betas.AsyncBetasResourceWithStreamingResponse:
        from .resources.betas import AsyncBetasResourceWithStreamingResponse

        return AsyncBetasResourceWithStreamingResponse(self._client.betas)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithStreamingResponse:
        from .resources.brands import AsyncBrandsResourceWithStreamingResponse

        return AsyncBrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)


Client = CheckoutIntents

AsyncClient = AsyncCheckoutIntents
