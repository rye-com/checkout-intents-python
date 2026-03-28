# CheckoutIntents

Types:

```python
from checkout_intents.types import (
    BaseCheckoutIntent,
    Buyer,
    CheckoutIntent,
    Money,
    Offer,
    PaymentMethod,
    VariantSelection,
)
```

Methods:

- <code title="post /api/v1/checkout-intents">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">create</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_create_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="get /api/v1/checkout-intents/{id}">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="get /api/v1/checkout-intents">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">list</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">SyncCursorPagination[CheckoutIntent]</a></code>
- <code title="post /api/v1/checkout-intents/{id}/payment">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">add_payment</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intent_add_payment_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="post /api/v1/checkout-intents/{id}/confirm">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">confirm</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intent_confirm_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="post /api/v1/checkout-intents/purchase">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">purchase</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_purchase_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code>client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">poll_until_completed</a>(id) -> CompletedCheckoutIntent | FailedCheckoutIntent</code>
- <code>client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">poll_until_awaiting_confirmation</a>(id) -> AwaitingConfirmationCheckoutIntent | FailedCheckoutIntent</code>
- <code>client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">create_and_poll</a>(\*\*params) -> AwaitingConfirmationCheckoutIntent | FailedCheckoutIntent</code>
- <code>client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">confirm_and_poll</a>(id, \*\*params) -> CompletedCheckoutIntent | FailedCheckoutIntent</code>

## Shipments

Methods:

- <code title="get /api/v1/checkout-intents/{id}/shipments">client.checkout_intents.shipments.<a href="./src/checkout_intents/resources/checkout_intents/shipments.py">list</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intents/shipment_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/shipment.py">SyncCursorPagination[Shipment]</a></code>

# Betas

Types:

```python
from checkout_intents.types import CheckoutSession
```

## CheckoutSessions

Methods:

- <code title="post /api/v1/betas/checkout-sessions">client.betas.checkout_sessions.<a href="./src/checkout_intents/resources/betas/checkout_sessions.py">create</a>(\*\*<a href="src/checkout_intents/types/betas/checkout_session_create_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_session.py">CheckoutSession</a></code>

# Brands

Types:

```python
from checkout_intents.types import BrandRetrieveResponse
```

Methods:

- <code title="get /api/v1/brands/domain/{domain}">client.brands.<a href="./src/checkout_intents/resources/brands.py">retrieve</a>(domain) -> <a href="./src/checkout_intents/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>

# Products

Types:

```python
from checkout_intents.types import (
    Product,
    ProductAvailability,
    ProductImage,
    ProductVariant,
    VariantDimension,
)
```

Methods:

- <code title="get /api/v1/products/lookup">client.products.<a href="./src/checkout_intents/resources/products.py">lookup</a>(\*\*<a href="src/checkout_intents/types/product_lookup_params.py">params</a>) -> <a href="./src/checkout_intents/types/product.py">Product</a></code>

# Shipments

Types:

```python
from checkout_intents.types import Shipment, ShipmentStatus, ShipmentTracking
```

Methods:

- <code title="get /api/v1/shipments/{id}">client.shipments.<a href="./src/checkout_intents/resources/shipments.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/shipment.py">Shipment</a></code>
- <code title="get /api/v1/shipments">client.shipments.<a href="./src/checkout_intents/resources/shipments.py">list</a>(\*\*<a href="src/checkout_intents/types/shipment_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/shipment.py">SyncCursorPagination[Shipment]</a></code>

# PaymentGateways

Types:

```python
from checkout_intents.types import PaymentGateway, PaymentGatewaySession
```

Methods:

- <code title="post /api/v1/payment-gateways/{gateway}/session">client.payment_gateways.<a href="./src/checkout_intents/resources/payment_gateways.py">create_session</a>(gateway) -> <a href="./src/checkout_intents/types/payment_gateway_session.py">PaymentGatewaySession</a></code>

# Billing

Types:

```python
from checkout_intents.types import BillingGetBalanceResponse, BillingListTransactionsResponse
```

Methods:

- <code title="get /api/v1/billing/balance">client.billing.<a href="./src/checkout_intents/resources/billing.py">get_balance</a>() -> <a href="./src/checkout_intents/types/billing_get_balance_response.py">BillingGetBalanceResponse</a></code>
- <code title="get /api/v1/billing/transactions">client.billing.<a href="./src/checkout_intents/resources/billing.py">list_transactions</a>(\*\*<a href="src/checkout_intents/types/billing_list_transactions_params.py">params</a>) -> <a href="./src/checkout_intents/types/billing_list_transactions_response.py">SyncCursorPagination[BillingListTransactionsResponse]</a></code>
