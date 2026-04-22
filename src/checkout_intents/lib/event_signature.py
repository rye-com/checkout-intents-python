from __future__ import annotations

import hmac
import hashlib

from .._exceptions import WebhookSignatureVerificationError
from ..types.event import Event

__all__ = ["unwrap_event"]

_SIGNATURE_PREFIX = "v0="


def unwrap_event(body: str | bytes, signature_header: str | None, secret: str) -> Event:
    """
    Verifies the webhook signature and parses the payload into an Event.

    Args:
        body: The raw request body. Must be the exact bytes/string received; do not
            decode or modify.
        signature_header: The value of the `x-rye-signature` HTTP header.
        secret: Your webhook secret key (typically from the `RYE_HMAC_SECRET_KEY`
            environment variable).

    Returns:
        The parsed Event if the signature is valid.

    Raises:
        WebhookSignatureVerificationError: If the signature is missing, malformed,
            or invalid.
    """
    if signature_header is None or not signature_header.startswith(_SIGNATURE_PREFIX):
        raise WebhookSignatureVerificationError(
            f"Invalid signature header format. Expected header starting with '{_SIGNATURE_PREFIX}'."
        )

    expected_signature = signature_header[len(_SIGNATURE_PREFIX) :]

    if isinstance(body, str):
        body_bytes = body.encode("utf-8")
    else:
        body_bytes = body

    computed_signature = hmac.new(
        secret.encode("utf-8"),
        body_bytes,
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(computed_signature, expected_signature):
        raise WebhookSignatureVerificationError(
            "Webhook signature verification failed. The signature does not match the payload."
        )

    try:
        return Event.model_validate_json(body_bytes)
    except Exception as e:
        raise WebhookSignatureVerificationError(f"Failed to parse webhook payload: {e}") from e
