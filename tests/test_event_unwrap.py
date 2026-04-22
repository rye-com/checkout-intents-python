# Test for events.unwrap() webhook signature verification

from __future__ import annotations

import hashlib
import hmac

import pytest

from checkout_intents import AsyncCheckoutIntents, CheckoutIntents, WebhookSignatureVerificationError


WEBHOOK_SECRET = "test_webhook_secret_key"

EVENT_PAYLOAD = """{
    "id": "evt_1234567890",
    "createdAt": "2026-03-25T00:00:00Z",
    "object": "event",
    "source": {
        "id": "ci_1234567890",
        "type": "checkout_intent"
    },
    "type": "checkout_intent.offer_retrieved"
}"""


def compute_signature(data: bytes, key: str) -> str:
    return hmac.new(key.encode("utf-8"), data, hashlib.sha256).hexdigest()


class TestEventsUnwrap:
    @pytest.fixture
    def client(self) -> CheckoutIntents:
        return CheckoutIntents(api_key="test", environment="staging")

    def test_unwrap_with_valid_signature(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")
        signature = compute_signature(body, WEBHOOK_SECRET)

        event = client.events.unwrap(body, f"v0={signature}", WEBHOOK_SECRET)

        assert event.id == "evt_1234567890"
        assert event.created_at == "2026-03-25T00:00:00Z"
        assert event.object == "event"
        assert event.source.id == "ci_1234567890"
        assert event.source.type == "checkout_intent"
        assert event.type == "checkout_intent.offer_retrieved"

    def test_unwrap_with_string_body(self, client: CheckoutIntents) -> None:
        signature = compute_signature(EVENT_PAYLOAD.encode("utf-8"), WEBHOOK_SECRET)

        event = client.events.unwrap(EVENT_PAYLOAD, f"v0={signature}", WEBHOOK_SECRET)

        assert event.id == "evt_1234567890"

    def test_unwrap_with_none_signature_header(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(body, None, WEBHOOK_SECRET)

        assert "Invalid signature header format" in str(exc_info.value)

    def test_unwrap_with_missing_prefix(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")
        signature = compute_signature(body, WEBHOOK_SECRET)

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(body, signature, WEBHOOK_SECRET)

        assert "Invalid signature header format" in str(exc_info.value)

    def test_unwrap_with_invalid_signature(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(body, "v0=invalid_signature", WEBHOOK_SECRET)

        assert "signature verification failed" in str(exc_info.value)

    def test_unwrap_with_wrong_secret(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")
        signature = compute_signature(body, WEBHOOK_SECRET)

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(body, f"v0={signature}", "wrong_secret")

        assert "signature verification failed" in str(exc_info.value)

    def test_unwrap_with_tampered_body(self, client: CheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")
        signature = compute_signature(body, WEBHOOK_SECRET)
        tampered_body = EVENT_PAYLOAD.replace("evt_1234567890", "evt_tampered")

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(tampered_body, f"v0={signature}", WEBHOOK_SECRET)

        assert "signature verification failed" in str(exc_info.value)

    def test_unwrap_with_invalid_json(self, client: CheckoutIntents) -> None:
        body = b"not valid json"
        signature = compute_signature(body, WEBHOOK_SECRET)

        with pytest.raises(WebhookSignatureVerificationError) as exc_info:
            client.events.unwrap(body, f"v0={signature}", WEBHOOK_SECRET)

        assert "Failed to parse webhook payload" in str(exc_info.value)

    def test_unwrap_with_real_webhook_payload(self, client: CheckoutIntents) -> None:
        body = '{"id":"evt_ci_acf8e2c44f4c4583bd5b58d291242bb2_awaiting_confirmation","object":"event","type":"checkout_intent.offer_retrieved","createdAt":"2026-04-21T03:27:50.000Z","source":{"type":"checkout_intent","id":"ci_acf8e2c44f4c4583bd5b58d291242bb2"}}'
        signature = "v0=a296fa9084469414e018aa8c33f68d315f88a0b503babb3825f7de87f473803e"
        secret = "6b2f15a9c9ee825fcf6f6447351a810c"

        event = client.events.unwrap(body, signature, secret)

        assert event.id == "evt_ci_acf8e2c44f4c4583bd5b58d291242bb2_awaiting_confirmation"
        assert event.type == "checkout_intent.offer_retrieved"
        assert event.source.id == "ci_acf8e2c44f4c4583bd5b58d291242bb2"
        assert event.source.type == "checkout_intent"


class TestAsyncEventsUnwrap:
    @pytest.fixture
    def async_client(self) -> AsyncCheckoutIntents:
        return AsyncCheckoutIntents(api_key="test", environment="staging")

    def test_unwrap_with_valid_signature(self, async_client: AsyncCheckoutIntents) -> None:
        body = EVENT_PAYLOAD.encode("utf-8")
        signature = compute_signature(body, WEBHOOK_SECRET)

        event = async_client.events.unwrap(body, f"v0={signature}", WEBHOOK_SECRET)

        assert event.id == "evt_1234567890"
        assert event.type == "checkout_intent.offer_retrieved"
