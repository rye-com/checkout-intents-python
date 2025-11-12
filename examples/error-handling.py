#!/usr/bin/env -S uv run python

"""
Handling polling timeouts and errors.

This example demonstrates:
- How to catch PollTimeoutError specifically
- How to access timeout error details
- How to configure polling parameters
- How to handle different error scenarios
- Best practices for error handling
"""

import os

from checkout_intents import CheckoutIntents, PollTimeoutError, CheckoutIntentsError


def main() -> None:
    """Demonstrate error handling for polling operations."""
    client = CheckoutIntents(
        api_key=os.getenv("CHECKOUT_INTENTS_API_KEY"),
    )

    print("Creating checkout intent...")

    intent = client.checkout_intents.create(
        buyer={
            "address1": "123 Main St",
            "city": "New York",
            "country": "US",
            "email": "john.doe@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "5555555555",
            "postal_code": "10001",
            "province": "NY",
        },
        product_url="https://flybyjing.com/collections/shop/products/sichuan-chili-crisp",
        quantity=1,
    )

    print(f"Created checkout intent: {intent.id}")

    try:
        print("\nPolling with immediate timeout (will timeout)...")

        # Poll with immediate timeout to demonstrate error handling
        client.checkout_intents.poll_until_awaiting_confirmation(
            intent.id,
            poll_interval=0,
            max_attempts=1,
        )

        print("✓ Polling succeeded (unexpected)")

    except PollTimeoutError as e:
        print("✗ Polling timed out as expected")
        print(f"\nPollTimeoutError details:")
        print(f"  Intent ID: {e.intent_id}")
        print(f"  Attempts made: {e.attempts}")
        print(f"  Time elapsed: {e.attempts * e.poll_interval}s")
        print(f"  Poll interval: {e.poll_interval}s")
        print(f"  Max attempts: {e.max_attempts}")
        print(f"\nError message:\n  {e}")

        print("\nTo fix this:")
        print("  - Increase max_attempts (e.g., 60 for ~5 minutes with 5s interval)")
        print("  - Increase poll_interval if you want less frequent checks")
        print("  - Use appropriate polling method (poll_until_awaiting_confirmation or poll_until_completed)")

        # You can also retrieve the intent manually to check its current state
        print(f"\nManually checking intent state...")
        current_intent = client.checkout_intents.retrieve(e.intent_id)
        print(f"  Current state: {current_intent.state}")

    except CheckoutIntentsError as e:
        # Catch other SDK errors (API errors, network errors, etc.)
        print(f"✗ Other error: {e}")


if __name__ == "__main__":
    main()
