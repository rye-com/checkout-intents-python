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
- <code title="post /api/v1/checkout-intents/{id}/confirm">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">confirm</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intent_confirm_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="post /api/v1/checkout-intents/purchase">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">purchase</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_purchase_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="get /api/v1/checkout-intents/{id}/order">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents/checkout_intents.py">retrieve_order</a>(id) -> <a href="./src/checkout_intents/types/order.py">Order</a></code>

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

# Orders

Types:

```python
from checkout_intents.types import Cancellation, Order
```

Methods:

- <code title="get /api/v1/orders/{id}">client.orders.<a href="./src/checkout_intents/resources/orders.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/order.py">Order</a></code>
- <code title="get /api/v1/orders">client.orders.<a href="./src/checkout_intents/resources/orders.py">list</a>(\*\*<a href="src/checkout_intents/types/order_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/order.py">SyncCursorPagination[Order]</a></code>
- <code title="post /api/v1/orders/{id}/cancel">client.orders.<a href="./src/checkout_intents/resources/orders.py">cancel</a>(id, \*\*<a href="src/checkout_intents/types/order_cancel_params.py">params</a>) -> <a href="./src/checkout_intents/types/cancellation.py">Cancellation</a></code>

# Products

Types:

```python
from checkout_intents.types import (
    Product,
    ProductAvailability,
    ProductImage,
    ProductSubscription,
    ProductSubscriptionProduct,
    ProductSubscriptionStore,
    ProductVariant,
    VariantDimension,
    ProductListSubscriptionsResponse,
)
```

Methods:

- <code title="get /api/v1/products/subscriptions">client.products.<a href="./src/checkout_intents/resources/products.py">list_subscriptions</a>() -> <a href="./src/checkout_intents/types/product_list_subscriptions_response.py">ProductListSubscriptionsResponse</a></code>
- <code title="get /api/v1/products/lookup">client.products.<a href="./src/checkout_intents/resources/products.py">lookup</a>(\*\*<a href="src/checkout_intents/types/product_lookup_params.py">params</a>) -> <a href="./src/checkout_intents/types/product.py">Product</a></code>
- <code title="post /api/v1/products/subscribe">client.products.<a href="./src/checkout_intents/resources/products.py">subscribe</a>(\*\*<a href="src/checkout_intents/types/product_subscribe_params.py">params</a>) -> <a href="./src/checkout_intents/types/product_subscription.py">ProductSubscription</a></code>
- <code title="post /api/v1/products/unsubscribe">client.products.<a href="./src/checkout_intents/resources/products.py">unsubscribe</a>(\*\*<a href="src/checkout_intents/types/product_unsubscribe_params.py">params</a>) -> <a href="./src/checkout_intents/types/product_subscription.py">ProductSubscription</a></code>

# Shipments

Types:

```python
from checkout_intents.types import Shipment, ShipmentStatus, ShipmentTracking
```

Methods:

- <code title="get /api/v1/shipments/{id}">client.shipments.<a href="./src/checkout_intents/resources/shipments.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/shipment.py">Shipment</a></code>
- <code title="get /api/v1/shipments">client.shipments.<a href="./src/checkout_intents/resources/shipments.py">list</a>(\*\*<a href="src/checkout_intents/types/shipment_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/shipment.py">SyncCursorPagination[Shipment]</a></code>

# Commissions

Types:

```python
from checkout_intents.types import Commission, CommissionStatus, CommissionType, SettlementDirection
```

Methods:

- <code title="get /api/v1/commissions">client.commissions.<a href="./src/checkout_intents/resources/commissions.py">list</a>(\*\*<a href="src/checkout_intents/types/commission_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/commission.py">SyncCursorPagination[Commission]</a></code>

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
from checkout_intents.types import (
    BillingCreateTopupInvoiceResponse,
    BillingGetBalanceResponse,
    BillingListTransactionsResponse,
)
```

Methods:

- <code title="delete /api/v1/billing/drawdown/topup/{invoiceId}">client.billing.<a href="./src/checkout_intents/resources/billing.py">cancel_topup_invoice</a>(invoice_id) -> None</code>
- <code title="post /api/v1/billing/drawdown/topup">client.billing.<a href="./src/checkout_intents/resources/billing.py">create_topup_invoice</a>(\*\*<a href="src/checkout_intents/types/billing_create_topup_invoice_params.py">params</a>) -> <a href="./src/checkout_intents/types/billing_create_topup_invoice_response.py">BillingCreateTopupInvoiceResponse</a></code>
- <code title="get /api/v1/billing/balance">client.billing.<a href="./src/checkout_intents/resources/billing.py">get_balance</a>() -> <a href="./src/checkout_intents/types/billing_get_balance_response.py">BillingGetBalanceResponse</a></code>
- <code title="get /api/v1/billing/transactions">client.billing.<a href="./src/checkout_intents/resources/billing.py">list_transactions</a>(\*\*<a href="src/checkout_intents/types/billing_list_transactions_params.py">params</a>) -> <a href="./src/checkout_intents/types/billing_list_transactions_response.py">SyncCursorPagination[BillingListTransactionsResponse]</a></code>

# Events

Types:

```python
from checkout_intents.types import Event
```

Methods:

- <code title="get /api/v1/events/{id}">client.events.<a href="./src/checkout_intents/resources/events.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/event.py">Event</a></code>
- <code title="get /api/v1/events">client.events.<a href="./src/checkout_intents/resources/events.py">list</a>(\*\*<a href="src/checkout_intents/types/event_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/event.py">SyncCursorPagination[Event]</a></code>

# MerchantConnectors

Types:

```python
from checkout_intents.types import InstallationLink
```

Methods:

- <code title="get /api/v1/merchant-connectors/{connector}/installation-link">client.merchant_connectors.<a href="./src/checkout_intents/resources/merchant_connectors.py">create_installation_link</a>(connector, \*\*<a href="src/checkout_intents/types/merchant_connector_create_installation_link_params.py">params</a>) -> <a href="./src/checkout_intents/types/installation_link.py">InstallationLink</a></code>

# Returns

Types:

```python
from checkout_intents.types import (
    Return,
    ReturnDenial,
    ReturnFailure,
    ReturnNextAction,
    ReturnReason,
    ReturnRefund,
    ReturnState,
    ReturnTimeline,
)
```

Methods:

- <code title="post /api/v1/returns">client.returns.<a href="./src/checkout_intents/resources/returns.py">create</a>(\*\*<a href="src/checkout_intents/types/return_create_params.py">params</a>) -> <a href="./src/checkout_intents/types/return_.py">Return</a></code>
- <code title="get /api/v1/returns/{returnId}">client.returns.<a href="./src/checkout_intents/resources/returns.py">retrieve</a>(return*id) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>

# TestHelpers

## Returns

Methods:

- <code title="post /api/v1/test-helpers/returns">client.test*helpers.returns.<a href="./src/checkout_intents/resources/test_helpers/returns.py">create</a>(\*\*<a href="src/checkout_intents/types/test_helpers/return_create_params.py">params</a>) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>
- <code title="post /api/v1/test-helpers/returns/{returnId}/approve">client.test*helpers.returns.<a href="./src/checkout_intents/resources/test_helpers/returns.py">approve</a>(return_id, \*\*<a href="src/checkout_intents/types/test_helpers/return_approve_params.py">params</a>) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>
- <code title="post /api/v1/test-helpers/returns/{returnId}/deny">client.test*helpers.returns.<a href="./src/checkout_intents/resources/test_helpers/returns.py">deny</a>(return_id, \*\*<a href="src/checkout_intents/types/test_helpers/return_deny_params.py">params</a>) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>
- <code title="post /api/v1/test-helpers/returns/{returnId}/fail">client.test*helpers.returns.<a href="./src/checkout_intents/resources/test_helpers/returns.py">fail</a>(return_id, \*\*<a href="src/checkout_intents/types/test_helpers/return_fail_params.py">params</a>) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>
- <code title="post /api/v1/test-helpers/returns/{returnId}/refund">client.test*helpers.returns.<a href="./src/checkout_intents/resources/test_helpers/returns.py">refund</a>(return_id, \*\*<a href="src/checkout_intents/types/test_helpers/return_refund_params.py">params</a>) -> <a href="./src/checkout_intents/types/return*.py">Return</a></code>

## Shipments

Types:

```python
from checkout_intents.types.test_helpers import ShipmentAdvanceResponse
```

Methods:

- <code title="post /api/v1/test-helpers/checkout-intents/{checkoutIntentId}/shipments/advance">client.test_helpers.shipments.<a href="./src/checkout_intents/resources/test_helpers/shipments.py">advance</a>(checkout_intent_id) -> <a href="./src/checkout_intents/types/test_helpers/shipment_advance_response.py">ShipmentAdvanceResponse</a></code>
