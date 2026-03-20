# Changelog

## 0.19.0 (2026-03-20)

Full Changelog: [v0.18.0...v0.19.0](https://github.com/rye-com/checkout-intents-python/compare/v0.18.0...v0.19.0)

### Features

* Add deliveryEstimate to shipping options in offers. ([ce9ab11](https://github.com/rye-com/checkout-intents-python/commit/ce9ab11cb94184ce809d525ae0286710dad39e59))

## 0.18.0 (2026-03-17)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/rye-com/checkout-intents-python/compare/v0.17.0...v0.18.0)

### Features

* Return 403 for non-drawdown developers on billing endpoints ([4af9f70](https://github.com/rye-com/checkout-intents-python/commit/4af9f70a83cdfdd43def3662642617779cf4bffc))
* Update shipment types in prep for tracking updates ([a7e961b](https://github.com/rye-com/checkout-intents-python/commit/a7e961bb3f6719b94f125ec1c282fd8afb65a9ef))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([f091341](https://github.com/rye-com/checkout-intents-python/commit/f091341965c422e2000ae91af8d59b6a90fecb17))
* **docs:** remove double-slash from server urls ([3085ed4](https://github.com/rye-com/checkout-intents-python/commit/3085ed4b85626da020827fe10717a90804121c99))
* **pydantic:** do not pass `by_alias` unless set ([9e0774e](https://github.com/rye-com/checkout-intents-python/commit/9e0774e3da803b64e61fa94fe023a2aa96fd1374))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([f1f6597](https://github.com/rye-com/checkout-intents-python/commit/f1f6597e19f6bac06300d4f8f7f6b783dc1495b0))
* **docs:** improve examples ([15cfd8e](https://github.com/rye-com/checkout-intents-python/commit/15cfd8ebdcca501f6663cfc66ebc911838d2234f))
* **internal:** tweak CI branches ([ddf8eaa](https://github.com/rye-com/checkout-intents-python/commit/ddf8eaa99e0fe5c002dfa18c45f5bec9f9deb5d5))
* **internal:** update tests ([c585a9f](https://github.com/rye-com/checkout-intents-python/commit/c585a9f6f2ed5573adcf6dd777e85b60964769fd))

## 0.17.0 (2026-03-06)

Full Changelog: [v0.16.1...v0.17.0](https://github.com/rye-com/checkout-intents-python/compare/v0.16.1...v0.17.0)

### Features

* Add variant models to Stainless SDK config ([4fd1821](https://github.com/rye-com/checkout-intents-python/commit/4fd1821d751e15c88a84fba019702d9da53a850a))
* add variant types and wire through extraction pipeline (RYE-6876) ([0ecd388](https://github.com/rye-com/checkout-intents-python/commit/0ecd38871fcfc812f7c9cd8bfb289ea3b4b161f2))
* Cut 1x Firestore read from offer retrieval ([c5a610e](https://github.com/rye-com/checkout-intents-python/commit/c5a610efca5222f15972d15b208079c33df01fe6))
* rename ProductVariant.attributes to dimensions ([fccf08a](https://github.com/rye-com/checkout-intents-python/commit/fccf08a50b07f2e648199ca14d04d29d02307741))


### Bug Fixes

* handle [@type](https://github.com/type) array and AggregateOffer array in JSON-LD parser ([d1d8800](https://github.com/rye-com/checkout-intents-python/commit/d1d880027e6ce8de295d76a587875ae2f8dc4d45))
* **internal:** duplicate definitions ([5c45e18](https://github.com/rye-com/checkout-intents-python/commit/5c45e1804fe1173a25f299c9e003ec15f6a17543))
* rename VariantDimension.name to label for consistency with VariantSelection ([bd38b39](https://github.com/rye-com/checkout-intents-python/commit/bd38b396452fcee10b30aeadd1dcc16a063610a4))


### Chores

* **internal:** improvements ([dd6b3be](https://github.com/rye-com/checkout-intents-python/commit/dd6b3be7b0b2b84761e1f8638538d8b1da9ed75d))

## 0.16.1 (2026-02-28)

Full Changelog: [v0.16.0...v0.16.1](https://github.com/rye-com/checkout-intents-python/compare/v0.16.0...v0.16.1)

### Chores

* **internal:** improvements ([64b6b21](https://github.com/rye-com/checkout-intents-python/commit/64b6b2105be66032a02e973fcb013b7645cdb90e))

## 0.16.0 (2026-02-27)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/rye-com/checkout-intents-python/compare/v0.15.0...v0.16.0)

### Features

* Add hidden billing API endpoints for drawdown balance and transactions ([8af9244](https://github.com/rye-com/checkout-intents-python/commit/8af9244c39eee35d47735c52d2e3e558f2d3142b))
* Added new shipments endpoint for tracking Amazon orders ([e5e8a46](https://github.com/rye-com/checkout-intents-python/commit/e5e8a46cb084e099530423cfe92ff4dcb6c52c91))
* proxy product images through Rye domain ([7913d19](https://github.com/rye-com/checkout-intents-python/commit/7913d19fb75ca691c2e58dcf4d9b5193038ce893))


### Chores

* **ci:** bump uv version ([b78c21e](https://github.com/rye-com/checkout-intents-python/commit/b78c21e0e62a1497e3b22ba48ddca4ee765dfe65))
* **internal:** add request options to SSE classes ([6fc9197](https://github.com/rye-com/checkout-intents-python/commit/6fc919750ac21e67366a5d19c0fddb41dd04262d))
* **internal:** improvements ([38698a0](https://github.com/rye-com/checkout-intents-python/commit/38698a04c3e6380ca38f5515161f5851d8d55edd))
* **internal:** improvements ([72e6cbe](https://github.com/rye-com/checkout-intents-python/commit/72e6cbe941247c433b3acd755add48edba1426a1))
* **internal:** improvements ([faf9197](https://github.com/rye-com/checkout-intents-python/commit/faf9197ad0b2316ea3f067f7f39fb37e857005ef))
* **internal:** make `test_proxy_environment_variables` more resilient ([43b003f](https://github.com/rye-com/checkout-intents-python/commit/43b003f9e79805509605019e0e0b6bbabba21f87))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([43020ec](https://github.com/rye-com/checkout-intents-python/commit/43020ec8a3b4c3c34c5afaeafd445ef8f57483a3))

## 0.15.0 (2026-02-24)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/rye-com/checkout-intents-python/compare/v0.14.0...v0.15.0)

### Features

* add merchants API endpoint ([466b30d](https://github.com/rye-com/checkout-intents-python/commit/466b30d55541062985872fdad7fde48f70a37b11))
* Add PaymentMethod support for Prava ([8491d49](https://github.com/rye-com/checkout-intents-python/commit/8491d49ed610c1753c14e5898cf9a0daac189787))
* Billing: Add BillingReconciliationService for expired drawdown orders ([1602c7b](https://github.com/rye-com/checkout-intents-python/commit/1602c7bf4a57249be075f246e1aa0a5308d510e6))
* Centralize Shopify domain resolution into ShopifyDomainResolver service ([344a639](https://github.com/rye-com/checkout-intents-python/commit/344a63969eb6639643c55aca7f9f2754a4c0be1f))
* Enable searching checkoutIntent by order Id on dev console ([f9e6a2b](https://github.com/rye-com/checkout-intents-python/commit/f9e6a2bd014add1daa175c7defa6f229129b0b38))
* Remove `shipments` from our stainless config ([f0a4141](https://github.com/rye-com/checkout-intents-python/commit/f0a414106be48277e79281407f4d6ed19894bc57))
* Remove duplicate method from controller ([f9d6de3](https://github.com/rye-com/checkout-intents-python/commit/f9d6de36b0f83b1d2d16684361ca0fca86dfa31f))
* Store estimated delivery date on completed checkout intent ([5b18341](https://github.com/rye-com/checkout-intents-python/commit/5b18341f6830bf88168878337694822d5f45b485))
* Unwrap `rd.bizrate.com` affiliate URLs ([3e3672e](https://github.com/rye-com/checkout-intents-python/commit/3e3672e7a877c6065309240a7af780cb2404ab51))
* Update return states to better reflect return lifecycle ([4a1056f](https://github.com/rye-com/checkout-intents-python/commit/4a1056f3383bf25a61753792f32f2e162032e4a6))
* wire up wizard layout and pass layout type through JWT ([1c2286b](https://github.com/rye-com/checkout-intents-python/commit/1c2286bdfd1bad99eebd65651fd93193b6be92c9))


### Bug Fixes

* **internal:** imports ([d5721ce](https://github.com/rye-com/checkout-intents-python/commit/d5721cea27ce3eb6177f400aba85948c0fd7f406))


### Chores

* format all `api.md` files ([73e7e50](https://github.com/rye-com/checkout-intents-python/commit/73e7e506e5a13b153fe2b374f255b97431505465))
* **internal:** bump dependencies ([f0f140a](https://github.com/rye-com/checkout-intents-python/commit/f0f140a95ce0e3fd5f530698ddab5800bc7d094a))
* **internal:** fix lint error on Python 3.14 ([95f86f0](https://github.com/rye-com/checkout-intents-python/commit/95f86f0d08d08528525fb7df107c57bdd5a2aa3c))
* **internal:** improvements ([e8ce927](https://github.com/rye-com/checkout-intents-python/commit/e8ce927f2493fb78c5a830932d63c5cd0bbd038a))
* **internal:** improvements ([dc9bb88](https://github.com/rye-com/checkout-intents-python/commit/dc9bb881f08e3119eed144affeef77dd8f75f869))
* **internal:** improvements ([f6a24cf](https://github.com/rye-com/checkout-intents-python/commit/f6a24cfacb70f21eef110c02a63203eeda8b9411))
* **internal:** move polling helpers to `lib/` dir ([980b367](https://github.com/rye-com/checkout-intents-python/commit/980b367a7713edda7979393f4d5e17435cea7b55))
* **internal:** remove mock server code ([0e7a4cc](https://github.com/rye-com/checkout-intents-python/commit/0e7a4cc1c15588ea25cdaef661befd538ec6ed3e))
* update mock server docs ([0f17c3f](https://github.com/rye-com/checkout-intents-python/commit/0f17c3f0b0fe8e2f02db05ea6c33a0ebce8a97a5))

## 0.14.0 (2026-02-05)

Full Changelog: [v0.13.1...v0.14.0](https://github.com/rye-com/checkout-intents-python/compare/v0.13.1...v0.14.0)

### Features

* Add stainless updates ([381560b](https://github.com/rye-com/checkout-intents-python/commit/381560bb9453bcece48d9bb95342c513a4b9ae43))
* **api:** add shipments tracking ([0d1e95a](https://github.com/rye-com/checkout-intents-python/commit/0d1e95a13e6c469f9608a3dff4b8a7d46b7862b2))
* Billing: Envelope payment processing fields ([f8b33da](https://github.com/rye-com/checkout-intents-python/commit/f8b33daa590cc016a9597e9a2d20ad21816d5293))
* Billing: Integrate drawdown payments in order flow ([252e1fa](https://github.com/rye-com/checkout-intents-python/commit/252e1fa3d916aaa45ba3715bd989dfe8aeaa89a4))
* integrate promo codes discovery to checkout intent flow ([6ad9468](https://github.com/rye-com/checkout-intents-python/commit/6ad9468f90ec2c5de698eebaeec3a7d4656ac1f2))
* Phase 3: Strategy Interface + Normalizer ([64987c1](https://github.com/rye-com/checkout-intents-python/commit/64987c13d11807eeb23f6e79baaa0179787d1f06))


### Bug Fixes

* **internal:** `PollTimeoutError` import ([b11f9b2](https://github.com/rye-com/checkout-intents-python/commit/b11f9b25a9c9fc57f13ca6d56d66a5bef141ee14))

## 0.13.1 (2026-01-30)

Full Changelog: [v0.13.0...v0.13.1](https://github.com/rye-com/checkout-intents-python/compare/v0.13.0...v0.13.1)

### Chores

* **docs:** rename "retrieve product" to "lookup product" ([6f7c761](https://github.com/rye-com/checkout-intents-python/commit/6f7c761b96d79e5971cade53f955dcd90e3c3378))

## 0.13.0 (2026-01-30)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/rye-com/checkout-intents-python/compare/v0.12.0...v0.13.0)

### Features

* **api:** introduce lookup product data endpoint ([a9083d2](https://github.com/rye-com/checkout-intents-python/commit/a9083d26b9f8648033a7f433e69936f5c6f1a3e9))
* **client:** add custom JSON encoder for extended type support ([06b80ca](https://github.com/rye-com/checkout-intents-python/commit/06b80ca98bd630f63245e62a96726a13b19084ed))
* Implement shipping profile -&gt; shipping option calculation ([b4aca4a](https://github.com/rye-com/checkout-intents-python/commit/b4aca4a8504dc530e00b2cd9ebe0f2ca77647bbe))


### Chores

* **internal:** rename `Product` type ([d9f34df](https://github.com/rye-com/checkout-intents-python/commit/d9f34dfc35d70140c380269a20e5214fca3bbb83))

## 0.12.0 (2026-01-24)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/rye-com/checkout-intents-python/compare/v0.11.0...v0.12.0)

### Features

* add support for idempotency for v2 api ([b7a09af](https://github.com/rye-com/checkout-intents-python/commit/b7a09af76927e67befdbe59566bddf7ab43240f0))
* **api:** introduce offerRetrievalEffort constraint ([5bc7a2c](https://github.com/rye-com/checkout-intents-python/commit/5bc7a2cc58c555dd4dcd5c0e3abf1f157cd61e8f))


### Chores

* **ci:** upgrade `actions/github-script` ([526d94a](https://github.com/rye-com/checkout-intents-python/commit/526d94ae385eb0e5f54124ca429651d55ce0ec53))
* **internal:** update `actions/checkout` version ([9eadb2e](https://github.com/rye-com/checkout-intents-python/commit/9eadb2e9a5a8abaad98be7567dd3dc195458cd53))

## 0.11.0 (2026-01-15)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/rye-com/checkout-intents-python/compare/v0.10.0...v0.11.0)

### Features

* **client:** add support for binary request streaming ([438d3db](https://github.com/rye-com/checkout-intents-python/commit/438d3db019a0e94f9f7d2ea204887c15ea34ec8d))


### Bug Fixes

* **api:** correctly type quantity as int ([c0cfd41](https://github.com/rye-com/checkout-intents-python/commit/c0cfd41c5d71765cf3d34eddd1c640282caa4c33))
* **api:** correctly type quantity as integer ([642e3f2](https://github.com/rye-com/checkout-intents-python/commit/642e3f206f4ba6120ff4f9892c8bc077f10fedfd))


### Chores

* **internal:** bump uv.lock version ([9e551da](https://github.com/rye-com/checkout-intents-python/commit/9e551da1755c820314699cc0d2ccaf8578f5f7f8))

## 0.10.0 (2026-01-06)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/rye-com/checkout-intents-python/compare/v0.9.0...v0.10.0)

### Features

* Fix Slack follow-up messages not posting to thread when initial message fails ([61f39ce](https://github.com/rye-com/checkout-intents-python/commit/61f39ce09ad720d99fb866eca1d30cd6fbe353fc))
* Improve JSDoc for checkout sessions ([dffa705](https://github.com/rye-com/checkout-intents-python/commit/dffa70546832f5f4c74ba0e1c3280a98739bc9bf))
* RYE-6466: Enrich tracked analytics context for the checkout intents api ([26ed61e](https://github.com/rye-com/checkout-intents-python/commit/26ed61e274b71f66d5c952561fe9565213aeed1b))
* Tidy API docs ([1ce6f5f](https://github.com/rye-com/checkout-intents-python/commit/1ce6f5fe5e7ca420b911b11d8bb5106e09e0ac40))

## 0.9.0 (2025-12-25)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/rye-com/checkout-intents-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** manual updates ([dc735cc](https://github.com/rye-com/checkout-intents-python/commit/dc735ccb8a0eaf4c46ffe8dd984fa4efb111e5d4))
* **api:** swap featured request ([c42f14b](https://github.com/rye-com/checkout-intents-python/commit/c42f14b1bed4bf417bb2c289e8ba62962086271b))

## 0.8.0 (2025-12-25)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/rye-com/checkout-intents-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** add support for purchase constraints ([6bfefb8](https://github.com/rye-com/checkout-intents-python/commit/6bfefb8494c05c7ea022f055e7b2644cf99de05e))

## 0.7.0 (2025-12-22)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/rye-com/checkout-intents-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** support promo codes in purchase endpoint ([db9b7ca](https://github.com/rye-com/checkout-intents-python/commit/db9b7caa613c20a0d516930551f89932be8f14d9))

## 0.6.0 (2025-12-22)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/rye-com/checkout-intents-python/compare/v0.5.0...v0.6.0)

### Features

* Include `/purchase` endpoint in our SDKs + docs ([7744f80](https://github.com/rye-com/checkout-intents-python/commit/7744f80e20bc5399d9b29e0bfb11d6b8f9997e38))


### Chores

* include polling helpers in raw resp classes ([67b0e3c](https://github.com/rye-com/checkout-intents-python/commit/67b0e3c1899a3d5415b126466fd5f525f61f2529))

## 0.5.0 (2025-12-19)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/rye-com/checkout-intents-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** add applied promo codes to offer ([abb5a98](https://github.com/rye-com/checkout-intents-python/commit/abb5a9815890e283050dff4a9760e76aa50af0ce))


### Chores

* **internal:** add `--fix` argument to lint script ([6a2fb37](https://github.com/rye-com/checkout-intents-python/commit/6a2fb37ee2d09820fd364e601616b1631f84bdb1))

## 0.4.0 (2025-12-18)

Full Changelog: [v0.3.3...v0.4.0](https://github.com/rye-com/checkout-intents-python/compare/v0.3.3...v0.4.0)

### Features

* Adds support for promo codes
* Add durable purchase workflow and supporting infrastructure ([9db3309](https://github.com/rye-com/checkout-intents-python/commit/9db33093a5825e56e0c900cde20c74c22fb3f932))

### Bug Fixes

* use async_to_httpx_files in patch method ([66f7a30](https://github.com/rye-com/checkout-intents-python/commit/66f7a30af6fcadd97c651ec3d911d74f4699360f))

## 0.3.3 (2025-12-17)

Full Changelog: [v0.3.2...v0.3.3](https://github.com/rye-com/checkout-intents-python/compare/v0.3.2...v0.3.3)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([1567425](https://github.com/rye-com/checkout-intents-python/commit/156742587303ed71cd6bd48cac88b289aa7b066a))


### Chores

* **docs:** use environment variables for authentication in code snippets ([1786fcf](https://github.com/rye-com/checkout-intents-python/commit/1786fcf0791f227d91a07e3aad06a302d16aa8e0))
* **internal:** add missing files argument to base client ([3af52aa](https://github.com/rye-com/checkout-intents-python/commit/3af52aa804ed204b5aeab65b996956448a2f0225))
* update lockfile ([3695089](https://github.com/rye-com/checkout-intents-python/commit/3695089432c17c48ebd52580651c023e75c44b8d))

## 0.3.2 (2025-11-28)

Full Changelog: [v0.3.1...v0.3.2](https://github.com/rye-com/checkout-intents-python/compare/v0.3.1...v0.3.2)

### Bug Fixes

* ensure streams are always closed ([33adf1a](https://github.com/rye-com/checkout-intents-python/commit/33adf1a16c46c3ec7463a1af36351efb76479b1f))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([61385ca](https://github.com/rye-com/checkout-intents-python/commit/61385ca14394f826160467cb3d50168b652263c9))

## 0.3.1 (2025-11-22)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/rye-com/checkout-intents-python/compare/v0.3.0...v0.3.1)

### Chores

* add Python 3.14 classifier and testing ([c5e5f48](https://github.com/rye-com/checkout-intents-python/commit/c5e5f4878211b638fad6db325ee1ea2971571c1e))

## 0.3.0 (2025-11-18)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/rye-com/checkout-intents-python/compare/v0.2.0...v0.3.0)

### Features

* Add python sdk target to stainless config ([eea256f](https://github.com/rye-com/checkout-intents-python/commit/eea256fef46bb35554488dba5a0818345096a66a))


### Bug Fixes

* **docs:** supply valid buyer details ([12d25b1](https://github.com/rye-com/checkout-intents-python/commit/12d25b12808a05aaedcf48fc97384b5da40ca7e4))


### Chores

* **internal:** format code ([445dea0](https://github.com/rye-com/checkout-intents-python/commit/445dea070ddcc8574d0304001e79bd25ca2f9de7))

## 0.2.0 (2025-11-13)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/rye-com/checkout-intents-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** add polling helpers ([35dfc75](https://github.com/rye-com/checkout-intents-python/commit/35dfc75a2335fabb2ad1bab4b14f3f231deca600))
* **api:** infer environment from api key ([341d678](https://github.com/rye-com/checkout-intents-python/commit/341d6781d5275abec09fcc6d4634d3725f096674))


### Bug Fixes

* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([004dd94](https://github.com/rye-com/checkout-intents-python/commit/004dd94cb5ec8647b21ba2568744bbb3e850c132))


### Chores

* **internal:** add type ignore annotations ([0d0990e](https://github.com/rye-com/checkout-intents-python/commit/0d0990e8b9f83614725366b69df65ca2c9aec402))
* **internal:** replace rye with uv ([6cc9fcc](https://github.com/rye-com/checkout-intents-python/commit/6cc9fcc05af9040b863187affc79323812af3d83))


### Documentation

* **api:** add polling helpers ([7bd9f19](https://github.com/rye-com/checkout-intents-python/commit/7bd9f19fbec2bdc289cc3ace4edfa10e0914b3a2))
* **internal:** replace rye with uv ([7fbabe6](https://github.com/rye-com/checkout-intents-python/commit/7fbabe69d822fc3577a1762804dae36e9ea7385a))

## 0.1.0 (2025-11-11)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/rye-com/checkout-intents-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([e4a0e20](https://github.com/rye-com/checkout-intents-python/commit/e4a0e206d7566f904ac22caea8954990ad5c7271))
* **api:** api update ([7d95f0d](https://github.com/rye-com/checkout-intents-python/commit/7d95f0db63098d4edf209c7291959eb5f08df44b))


### Chores

* configure new SDK language ([a8f36d4](https://github.com/rye-com/checkout-intents-python/commit/a8f36d46dc5c0d3e868d289132bb83465736d0f5))
* update SDK settings ([5271e8a](https://github.com/rye-com/checkout-intents-python/commit/5271e8aa9f149e67b203919039afb2f61deca5e2))
* update SDK settings ([949efc6](https://github.com/rye-com/checkout-intents-python/commit/949efc6b67a53d856d11214bc6a924d879c2dfab))
