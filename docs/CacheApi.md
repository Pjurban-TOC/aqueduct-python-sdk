# aqueduct_sdk.CacheApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cache_events**](CacheApi.md#get_cache_events) | **GET** /api/v1/cache/events | Get recent cache events
[**get_cache_stats**](CacheApi.md#get_cache_stats) | **GET** /api/v1/cache/stats | Get cache statistics
[**invalidate_cache**](CacheApi.md#invalidate_cache) | **POST** /api/v1/cache/invalidate | Invalidate cache entries
[**invalidate_cache_by_pattern**](CacheApi.md#invalidate_cache_by_pattern) | **POST** /api/v1/cache/invalidate/pattern | Invalidate cache by pattern
[**invalidate_response_cache**](CacheApi.md#invalidate_response_cache) | **DELETE** /v1/cache | Invalidate LLM response cache
[**invalidate_tenant_cache**](CacheApi.md#invalidate_tenant_cache) | **POST** /api/v1/cache/invalidate/tenant/{tenant_id} | Invalidate all cache for a tenant
[**stream_cache_invalidations**](CacheApi.md#stream_cache_invalidations) | **GET** /api/v1/cache/ws/invalidations | Real-time cache invalidation event stream (WebSocket)


# **get_cache_events**
> GetCacheEvents200Response get_cache_events(limit=limit)

Get recent cache events

Returns recent cache invalidation events for monitoring and debugging.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.get_cache_events200_response import GetCacheEvents200Response
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)
    limit = 50 # int | Maximum number of events to return. (optional) (default to 50)

    try:
        # Get recent cache events
        api_response = await api_instance.get_cache_events(limit=limit)
        print("The response of CacheApi->get_cache_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->get_cache_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of events to return. | [optional] [default to 50]

### Return type

[**GetCacheEvents200Response**](GetCacheEvents200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cache events. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cache_stats**
> GetCacheStats200Response get_cache_stats()

Get cache statistics

Returns cache utilization statistics including hit rates, size, and eviction counts.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.get_cache_stats200_response import GetCacheStats200Response
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)

    try:
        # Get cache statistics
        api_response = await api_instance.get_cache_stats()
        print("The response of CacheApi->get_cache_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->get_cache_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCacheStats200Response**](GetCacheStats200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cache statistics. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_cache**
> InvalidateCache200Response invalidate_cache(invalidate_cache_request)

Invalidate cache entries

Invalidates cache entries matching the specified pattern or keys.
Tenant cache isolation is strictly enforced.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.invalidate_cache200_response import InvalidateCache200Response
from aqueduct_sdk.models.invalidate_cache_request import InvalidateCacheRequest
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)
    invalidate_cache_request = {"pattern":"tenant:tnt_acme-corp_a1b2c3:*","keys":["tenant:tnt_acme-corp_a1b2c3:model:gpt-4o:config"],"tags":["inference","model-config"]} # InvalidateCacheRequest | 

    try:
        # Invalidate cache entries
        api_response = await api_instance.invalidate_cache(invalidate_cache_request)
        print("The response of CacheApi->invalidate_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->invalidate_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_cache_request** | [**InvalidateCacheRequest**](InvalidateCacheRequest.md)|  | 

### Return type

[**InvalidateCache200Response**](InvalidateCache200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidation result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_cache_by_pattern**
> InvalidateCacheByPattern200Response invalidate_cache_by_pattern(invalidate_cache_by_pattern_request)

Invalidate cache by pattern

Invalidates cache entries matching a glob pattern.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.invalidate_cache_by_pattern200_response import InvalidateCacheByPattern200Response
from aqueduct_sdk.models.invalidate_cache_by_pattern_request import InvalidateCacheByPatternRequest
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)
    invalidate_cache_by_pattern_request = {"pattern":"model:gpt-4o:*"} # InvalidateCacheByPatternRequest | 

    try:
        # Invalidate cache by pattern
        api_response = await api_instance.invalidate_cache_by_pattern(invalidate_cache_by_pattern_request)
        print("The response of CacheApi->invalidate_cache_by_pattern:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->invalidate_cache_by_pattern: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invalidate_cache_by_pattern_request** | [**InvalidateCacheByPatternRequest**](InvalidateCacheByPatternRequest.md)|  | 

### Return type

[**InvalidateCacheByPattern200Response**](InvalidateCacheByPattern200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pattern invalidation result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_response_cache**
> InvalidateResponseCache200Response invalidate_response_cache(model=model)

Invalidate LLM response cache

Clears cached LLM responses for the caller's tenant. The tenant is always
derived from the caller's JWT — callers cannot clear another tenant's cache.

Use the optional `model` query parameter to scope invalidation to a specific
model (e.g., clear only `gpt-4o` cache entries while keeping others).

This endpoint operates on the model-router's in-memory response cache, not
the distributed cache-invalidator service.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.invalidate_response_cache200_response import InvalidateResponseCache200Response
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)
    model = 'gpt-4o' # str | Only invalidate cache entries for this model. If omitted, all models for the caller's tenant are cleared. (optional)

    try:
        # Invalidate LLM response cache
        api_response = await api_instance.invalidate_response_cache(model=model)
        print("The response of CacheApi->invalidate_response_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->invalidate_response_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Only invalidate cache entries for this model. If omitted, all models for the caller&#39;s tenant are cleared. | [optional] 

### Return type

[**InvalidateResponseCache200Response**](InvalidateResponseCache200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidation result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**405** | Method not allowed. Only DELETE is supported. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_tenant_cache**
> InvalidateTenantCache200Response invalidate_tenant_cache(tenant_id)

Invalidate all cache for a tenant

Invalidates all cache entries scoped to a specific tenant.
Tenant cache isolation prevents cross-tenant cache poisoning.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.invalidate_tenant_cache200_response import InvalidateTenantCache200Response
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # Invalidate all cache for a tenant
        api_response = await api_instance.invalidate_tenant_cache(tenant_id)
        print("The response of CacheApi->invalidate_tenant_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheApi->invalidate_tenant_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**InvalidateTenantCache200Response**](InvalidateTenantCache200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant cache invalidated. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_cache_invalidations**
> stream_cache_invalidations()

Real-time cache invalidation event stream (WebSocket)

Upgrades to a WebSocket connection for real-time cache invalidation event
streaming. This is a WebSocket endpoint; clients must send an HTTP
`Upgrade: websocket` request.

**Status:** This endpoint is registered but not yet fully implemented
(returns 501 until WebSocket support is wired up).

Once implemented, the server will push invalidation events as they occur:

**Server -> Client messages (JSON):**
```json
{
  "event_type": "invalidation",
  "pattern": "tenant:tnt_acme-corp_a1b2c3:*",
  "keys_affected": 42,
  "tenant_id": "tnt_acme-corp_a1b2c3",
  "timestamp": "2026-03-19T12:00:00Z"
}
```

**Event types:** `invalidation`, `eviction`, `expiration`.

This allows dashboards and monitoring tools to react to cache state changes
in real time without polling the `/api/v1/cache/events` REST endpoint.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.CacheApi(api_client)

    try:
        # Real-time cache invalidation event stream (WebSocket)
        await api_instance.stream_cache_invalidations()
    except Exception as e:
        print("Exception when calling CacheApi->stream_cache_invalidations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | Switching Protocols. WebSocket connection established. |  -  |
**200** | WebSocket connection active (upgrade succeeded). This status is not returned directly; the connection upgrades via 101. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**501** | WebSocket support not yet implemented. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

