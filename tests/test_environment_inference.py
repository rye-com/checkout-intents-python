from __future__ import annotations

import pytest

from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents._exceptions import CheckoutIntentsError


class TestEnvironmentInference:
    """Tests for automatic environment inference from API keys"""

    def test_infers_staging_from_api_key(self) -> None:
        """Test that staging environment is inferred from RYE/staging- API key"""
        client = CheckoutIntents(
            api_key="RYE/staging-test1234567890",
            _strict_response_validation=True,
        )
        assert client._environment == "staging"
        assert str(client.base_url) == "https://staging.api.rye.com/"
        client.close()

    def test_infers_production_from_api_key(self) -> None:
        """Test that production environment is inferred from RYE/production- API key"""
        client = CheckoutIntents(
            api_key="RYE/production-test1234567890",
            _strict_response_validation=True,
        )
        assert client._environment == "production"
        assert str(client.base_url) == "https://api.rye.com/"
        client.close()

    def test_defaults_to_staging_for_non_matching_api_key(self) -> None:
        """Test that client defaults to staging when API key doesn't match pattern"""
        client = CheckoutIntents(
            api_key="some-random-api-key",
            _strict_response_validation=True,
        )
        assert client._environment == "staging"
        assert str(client.base_url) == "https://staging.api.rye.com/"
        client.close()

    def test_explicit_environment_overrides_inferred(self) -> None:
        """Test that explicitly provided environment takes precedence (when matching)"""
        client = CheckoutIntents(
            api_key="RYE/staging-test1234567890",
            environment="staging",
            _strict_response_validation=True,
        )
        assert client._environment == "staging"
        assert str(client.base_url) == "https://staging.api.rye.com/"
        client.close()

    def test_environment_mismatch_raises_error(self) -> None:
        """Test that mismatched environment and API key raises an error"""
        with pytest.raises(
            CheckoutIntentsError,
            match=r"Environment mismatch: API key is for 'staging' environment but 'environment' option is set to 'production'",
        ):
            CheckoutIntents(
                api_key="RYE/staging-test1234567890",
                environment="production",
                _strict_response_validation=True,
            )

    def test_environment_mismatch_opposite_direction(self) -> None:
        """Test that mismatched environment raises error (production key with staging env)"""
        with pytest.raises(
            CheckoutIntentsError,
            match=r"Environment mismatch: API key is for 'production' environment but 'environment' option is set to 'staging'",
        ):
            CheckoutIntents(
                api_key="RYE/production-test1234567890",
                environment="staging",
                _strict_response_validation=True,
            )

    def test_explicit_production_with_matching_key(self) -> None:
        """Test that explicitly provided production environment works with production key"""
        client = CheckoutIntents(
            api_key="RYE/production-test1234567890",
            environment="production",
            _strict_response_validation=True,
        )
        assert client._environment == "production"
        assert str(client.base_url) == "https://api.rye.com/"
        client.close()

    def test_base_url_overrides_inferred_environment(self) -> None:
        """Test that explicit base_url takes precedence over inferred environment"""
        client = CheckoutIntents(
            api_key="RYE/production-test1234567890",
            base_url="https://custom.api.com/",
            _strict_response_validation=True,
        )
        assert str(client.base_url) == "https://custom.api.com/"
        client.close()


class TestAsyncEnvironmentInference:
    """Tests for automatic environment inference from API keys in async client"""

    async def test_infers_staging_from_api_key(self) -> None:
        """Test that staging environment is inferred from RYE/staging- API key"""
        client = AsyncCheckoutIntents(
            api_key="RYE/staging-test1234567890",
            _strict_response_validation=True,
        )
        assert client._environment == "staging"
        assert str(client.base_url) == "https://staging.api.rye.com/"
        await client.close()

    async def test_infers_production_from_api_key(self) -> None:
        """Test that production environment is inferred from RYE/production- API key"""
        client = AsyncCheckoutIntents(
            api_key="RYE/production-test1234567890",
            _strict_response_validation=True,
        )
        assert client._environment == "production"
        assert str(client.base_url) == "https://api.rye.com/"
        await client.close()

    async def test_defaults_to_staging_for_non_matching_api_key(self) -> None:
        """Test that client defaults to staging when API key doesn't match pattern"""
        client = AsyncCheckoutIntents(
            api_key="some-random-api-key",
            _strict_response_validation=True,
        )
        assert client._environment == "staging"
        assert str(client.base_url) == "https://staging.api.rye.com/"
        await client.close()

    async def test_environment_mismatch_raises_error(self) -> None:
        """Test that mismatched environment and API key raises an error"""
        with pytest.raises(
            CheckoutIntentsError,
            match=r"Environment mismatch: API key is for 'staging' environment but 'environment' option is set to 'production'",
        ):
            AsyncCheckoutIntents(
                api_key="RYE/staging-test1234567890",
                environment="production",
                _strict_response_validation=True,
            )

    async def test_explicit_production_with_matching_key(self) -> None:
        """Test that explicitly provided production environment works with production key"""
        client = AsyncCheckoutIntents(
            api_key="RYE/production-test1234567890",
            environment="production",
            _strict_response_validation=True,
        )
        assert client._environment == "production"
        assert str(client.base_url) == "https://api.rye.com/"
        await client.close()

    async def test_base_url_overrides_inferred_environment(self) -> None:
        """Test that explicit base_url takes precedence over inferred environment"""
        client = AsyncCheckoutIntents(
            api_key="RYE/production-test1234567890",
            base_url="https://custom.api.com/",
            _strict_response_validation=True,
        )
        assert str(client.base_url) == "https://custom.api.com/"
        await client.close()
