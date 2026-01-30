# Changelog

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
