#!/usr/bin/env -S uv run python

"""
Recommended checkout flow (two-phase):
1. Create checkout intent and poll until offer is ready
2. Review pricing with user
3. Confirm with payment and poll until completion

This follows the Rye documented checkout flow.
"""

import os

from checkout_intents import CheckoutIntents


def main() -> None:
    """Demonstrate the complete two-phase checkout flow."""
    client = CheckoutIntents(
        api_key=os.getenv("CHECKOUT_INTENTS_API_KEY"),
    )

    # Phase 1: Create checkout intent and wait for offer
    print("Creating checkout intent...")

    intent = client.checkout_intents.create_and_poll(
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

    print(f"Checkout intent created: {intent.id}")
    print(f"State: {intent.state}")

    # Handle failure during offer retrieval
    if intent.state == "failed":
        print(f"Failed to retrieve offer: {intent.failure_reason}")
        return

    # Review the offer with the user before confirming
    if hasattr(intent, "offer"):
        print("\nOffer Details:")
        print(f"  Subtotal: {intent.offer.cost.subtotal}")
        print(f"  Shipping: {intent.offer.cost.shipping or intent.offer.shipping}")
        print(f"  Tax: {intent.offer.cost.tax}")
        print(f"  Total: {intent.offer.cost.total}")

    # Phase 2: User confirms, complete the checkout
    print("\nConfirming checkout...")

    completed = client.checkout_intents.confirm_and_poll(
        intent.id,
        payment_method={
            "type": "stripe_token",
            "stripe_token": "tok_visa",  # Use tok_visa in staging
        },
    )

    print(f"Final state: {completed.state}")

    if completed.state == "completed":
        print("✓ Order placed successfully!")
    elif completed.state == "failed":
        print(f"✗ Order failed: {completed.failure_reason}")


if __name__ == "__main__":
    main()
