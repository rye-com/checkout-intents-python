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

- <code title="post /api/v1/checkout-intents">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">create</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_create_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="get /api/v1/checkout-intents/{id}">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">retrieve</a>(id) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="get /api/v1/checkout-intents">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">list</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_list_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">SyncCursorPagination[CheckoutIntent]</a></code>
- <code title="post /api/v1/checkout-intents/{id}/payment">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">add_payment</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intent_add_payment_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="post /api/v1/checkout-intents/{id}/confirm">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">confirm</a>(id, \*\*<a href="src/checkout_intents/types/checkout_intent_confirm_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>
- <code title="post /api/v1/checkout-intents/purchase">client.checkout_intents.<a href="./src/checkout_intents/resources/checkout_intents.py">purchase</a>(\*\*<a href="src/checkout_intents/types/checkout_intent_purchase_params.py">params</a>) -> <a href="./src/checkout_intents/types/checkout_intent.py">CheckoutIntent</a></code>

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
from checkout_intents.types import Product, ProductAvailability, ProductImage
```

Methods:

- <code title="get /api/v1/products/lookup">client.products.<a href="./src/checkout_intents/resources/products.py">lookup</a>(\*\*<a href="src/checkout_intents/types/product_lookup_params.py">params</a>) -> <a href="./src/checkout_intents/types/product.py">Product</a></code>
