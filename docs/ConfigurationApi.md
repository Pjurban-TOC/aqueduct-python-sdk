# aqueduct_sdk.ConfigurationApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config**](ConfigurationApi.md#create_config) | **POST** /api/v1/config | Create a configuration entry
[**delete_config**](ConfigurationApi.md#delete_config) | **DELETE** /api/v1/config/{key} | Delete a configuration entry
[**delete_tenant_config_override**](ConfigurationApi.md#delete_tenant_config_override) | **DELETE** /api/v1/tenants/{tenant_id}/config/{key} | Delete a tenant configuration override
[**evaluate_flag**](ConfigurationApi.md#evaluate_flag) | **GET** /api/v1/flags/{flag} | Evaluate a feature flag
[**get_config**](ConfigurationApi.md#get_config) | **GET** /api/v1/config/{key} | Get configuration entry by key
[**get_tenant_merged_config**](ConfigurationApi.md#get_tenant_merged_config) | **GET** /api/v1/tenants/{tenant_id}/config | Get merged tenant configuration
[**list_config_audit**](ConfigurationApi.md#list_config_audit) | **GET** /api/v1/audit | List configuration audit log
[**list_config_versions**](ConfigurationApi.md#list_config_versions) | **GET** /api/v1/config/{key}/versions | List version history for a configuration entry
[**list_configs**](ConfigurationApi.md#list_configs) | **GET** /api/v1/config | List configuration entries
[**list_flags**](ConfigurationApi.md#list_flags) | **GET** /api/v1/flags | List all feature flags
[**rollback_config**](ConfigurationApi.md#rollback_config) | **POST** /api/v1/config/{key}/rollback | Rollback configuration to a previous version
[**set_global_flag**](ConfigurationApi.md#set_global_flag) | **PUT** /api/v1/flags/{flag} | Set global feature flag value
[**set_tenant_config_override**](ConfigurationApi.md#set_tenant_config_override) | **PUT** /api/v1/tenants/{tenant_id}/config/{key} | Set a tenant configuration override
[**set_tenant_flag_override**](ConfigurationApi.md#set_tenant_flag_override) | **PUT** /api/v1/flags/{flag}/tenant/{tenant_id} | Set tenant-specific feature flag override
[**update_config**](ConfigurationApi.md#update_config) | **PUT** /api/v1/config/{key} | Update a configuration entry


# **create_config**
> ConfigEntry create_config(create_config_request)

Create a configuration entry

Creates a new configuration entry with versioning. The initial version
is 1. All changes are recorded in the config audit log per
ISpec [arXiv:2512.17259] policy-as-code requirements.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_entry import ConfigEntry
from aqueduct_sdk.models.create_config_request import CreateConfigRequest
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    create_config_request = {"key":"auth.session_timeout_minutes","value":30,"type":"int","description":"Session timeout in minutes for all tenants"} # CreateConfigRequest | 

    try:
        # Create a configuration entry
        api_response = await api_instance.create_config(create_config_request)
        print("The response of ConfigurationApi->create_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->create_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_config_request** | [**CreateConfigRequest**](CreateConfigRequest.md)|  | 

### Return type

[**ConfigEntry**](ConfigEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Configuration entry created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config**
> delete_config(key)

Delete a configuration entry

Permanently removes a configuration entry and all its version history.

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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.

    try:
        # Delete a configuration entry
        await api_instance.delete_config(key)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 

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
**204** | Configuration entry deleted. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_config_override**
> delete_tenant_config_override(tenant_id, key)

Delete a tenant configuration override

Removes a tenant-specific override, reverting to the global default.

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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.

    try:
        # Delete a tenant configuration override
        await api_instance.delete_tenant_config_override(tenant_id, key)
    except Exception as e:
        print("Exception when calling ConfigurationApi->delete_tenant_config_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 

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
**204** | Override deleted. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_flag**
> FlagEvaluationResponse evaluate_flag(flag, tenant_id=tenant_id)

Evaluate a feature flag

Evaluates a feature flag, optionally for a specific tenant. Tenant
overrides take precedence over global flag values.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.flag_evaluation_response import FlagEvaluationResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    flag = 'enable-rag-v2' # str | Feature flag name.
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Filter or scope results to a specific tenant. (optional)

    try:
        # Evaluate a feature flag
        api_response = await api_instance.evaluate_flag(flag, tenant_id=tenant_id)
        print("The response of ConfigurationApi->evaluate_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->evaluate_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag** | **str**| Feature flag name. | 
 **tenant_id** | **str**| Filter or scope results to a specific tenant. | [optional] 

### Return type

[**FlagEvaluationResponse**](FlagEvaluationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag evaluation result. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> ConfigEntry get_config(key)

Get configuration entry by key

Returns a single configuration entry by its key.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_entry import ConfigEntry
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.

    try:
        # Get configuration entry by key
        api_response = await api_instance.get_config(key)
        print("The response of ConfigurationApi->get_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 

### Return type

[**ConfigEntry**](ConfigEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration entry. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_merged_config**
> ConfigListResponse get_tenant_merged_config(tenant_id)

Get merged tenant configuration

Returns the effective configuration for a tenant by merging global
defaults with tenant-specific overrides. Overrides take precedence.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_list_response import ConfigListResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # Get merged tenant configuration
        api_response = await api_instance.get_tenant_merged_config(tenant_id)
        print("The response of ConfigurationApi->get_tenant_merged_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->get_tenant_merged_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**ConfigListResponse**](ConfigListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Merged tenant configuration. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_audit**
> ConfigAuditListResponse list_config_audit(key=key, tenant_id=tenant_id, limit=limit, cursor=cursor)

List configuration audit log

Returns the audit trail for configuration changes. Tracks create,
update, delete, and rollback operations across all config entries.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_audit_list_response import ConfigAuditListResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'key_example' # str | Filter by configuration key. (optional)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Filter or scope results to a specific tenant. (optional)
    limit = 20 # int | Maximum entries to return. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List configuration audit log
        api_response = await api_instance.list_config_audit(key=key, tenant_id=tenant_id, limit=limit, cursor=cursor)
        print("The response of ConfigurationApi->list_config_audit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->list_config_audit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Filter by configuration key. | [optional] 
 **tenant_id** | **str**| Filter or scope results to a specific tenant. | [optional] 
 **limit** | **int**| Maximum entries to return. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**ConfigAuditListResponse**](ConfigAuditListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration audit log. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_versions**
> ConfigVersionListResponse list_config_versions(key, page_size=page_size, cursor=cursor)

List version history for a configuration entry

Returns the full version history for a configuration key, ordered by
version number descending. Supports audit trail requirements per
TRiSM [arXiv:2506.04133] model lineage tracking.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_version_list_response import ConfigVersionListResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List version history for a configuration entry
        api_response = await api_instance.list_config_versions(key, page_size=page_size, cursor=cursor)
        print("The response of ConfigurationApi->list_config_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->list_config_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**ConfigVersionListResponse**](ConfigVersionListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version history list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configs**
> ConfigListResponse list_configs(prefix=prefix, page_size=page_size, cursor=cursor)

List configuration entries

Returns a paginated list of all configuration entries, optionally filtered by key prefix.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_list_response import ConfigListResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    prefix = 'auth.' # str | Filter by key prefix (e.g., `auth.` returns all auth-related config). (optional)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List configuration entries
        api_response = await api_instance.list_configs(prefix=prefix, page_size=page_size, cursor=cursor)
        print("The response of ConfigurationApi->list_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->list_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| Filter by key prefix (e.g., &#x60;auth.&#x60; returns all auth-related config). | [optional] 
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**ConfigListResponse**](ConfigListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated configuration list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_flags**
> FeatureFlagListResponse list_flags()

List all feature flags

Returns all registered feature flags with their current global state.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.feature_flag_list_response import FeatureFlagListResponse
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)

    try:
        # List all feature flags
        api_response = await api_instance.list_flags()
        print("The response of ConfigurationApi->list_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->list_flags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FeatureFlagListResponse**](FeatureFlagListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Feature flag list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_config**
> ConfigEntry rollback_config(key, rollback_request)

Rollback configuration to a previous version

Rolls back a configuration entry to the specified version number.
Creates a new version with the rolled-back value.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_entry import ConfigEntry
from aqueduct_sdk.models.rollback_request import RollbackRequest
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.
    rollback_request = {"version":2} # RollbackRequest | 

    try:
        # Rollback configuration to a previous version
        api_response = await api_instance.rollback_config(key, rollback_request)
        print("The response of ConfigurationApi->rollback_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->rollback_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 
 **rollback_request** | [**RollbackRequest**](RollbackRequest.md)|  | 

### Return type

[**ConfigEntry**](ConfigEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration rolled back successfully. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_global_flag**
> FeatureFlag set_global_flag(flag, set_flag_request)

Set global feature flag value

Sets the global (default) value for a feature flag.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.feature_flag import FeatureFlag
from aqueduct_sdk.models.set_flag_request import SetFlagRequest
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    flag = 'enable-rag-v2' # str | Feature flag name.
    set_flag_request = {"enabled":true,"description":"Enable RAG v2 hybrid search globally"} # SetFlagRequest | 

    try:
        # Set global feature flag value
        api_response = await api_instance.set_global_flag(flag, set_flag_request)
        print("The response of ConfigurationApi->set_global_flag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->set_global_flag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag** | **str**| Feature flag name. | 
 **set_flag_request** | [**SetFlagRequest**](SetFlagRequest.md)|  | 

### Return type

[**FeatureFlag**](FeatureFlag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flag updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_config_override**
> SetTenantConfigOverride200Response set_tenant_config_override(tenant_id, key, set_override_request)

Set a tenant configuration override

Sets a tenant-specific override for a configuration key. The override
takes precedence over the global value when the merged config is read.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.set_override_request import SetOverrideRequest
from aqueduct_sdk.models.set_tenant_config_override200_response import SetTenantConfigOverride200Response
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.
    set_override_request = {"value":15,"type":"int","description":"Stricter session timeout for this tenant"} # SetOverrideRequest | 

    try:
        # Set a tenant configuration override
        api_response = await api_instance.set_tenant_config_override(tenant_id, key, set_override_request)
        print("The response of ConfigurationApi->set_tenant_config_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->set_tenant_config_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 
 **set_override_request** | [**SetOverrideRequest**](SetOverrideRequest.md)|  | 

### Return type

[**SetTenantConfigOverride200Response**](SetTenantConfigOverride200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Override set. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_flag_override**
> SetTenantFlagOverride200Response set_tenant_flag_override(flag, tenant_id, set_flag_request)

Set tenant-specific feature flag override

Overrides a feature flag value for a specific tenant. The override
takes precedence over the global flag value during evaluation.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.set_flag_request import SetFlagRequest
from aqueduct_sdk.models.set_tenant_flag_override200_response import SetTenantFlagOverride200Response
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    flag = 'enable-rag-v2' # str | Feature flag name.
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    set_flag_request = {"enabled":false,"description":"Disable RAG v2 for this tenant pending migration"} # SetFlagRequest | 

    try:
        # Set tenant-specific feature flag override
        api_response = await api_instance.set_tenant_flag_override(flag, tenant_id, set_flag_request)
        print("The response of ConfigurationApi->set_tenant_flag_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->set_tenant_flag_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flag** | **str**| Feature flag name. | 
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **set_flag_request** | [**SetFlagRequest**](SetFlagRequest.md)|  | 

### Return type

[**SetTenantFlagOverride200Response**](SetTenantFlagOverride200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant flag override set. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config**
> ConfigEntry update_config(key, config_update_config_request)

Update a configuration entry

Updates an existing configuration entry. A new version is created
automatically. The previous version is preserved in the version history.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.config_entry import ConfigEntry
from aqueduct_sdk.models.config_update_config_request import ConfigUpdateConfigRequest
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
    api_instance = aqueduct_sdk.ConfigurationApi(api_client)
    key = 'auth.session_timeout_minutes' # str | Configuration key matching `^[a-zA-Z0-9._-]+$`.
    config_update_config_request = {"value":60,"type":"int","description":"Increased session timeout to 60 minutes"} # ConfigUpdateConfigRequest | 

    try:
        # Update a configuration entry
        api_response = await api_instance.update_config(key, config_update_config_request)
        print("The response of ConfigurationApi->update_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationApi->update_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Configuration key matching &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 
 **config_update_config_request** | [**ConfigUpdateConfigRequest**](ConfigUpdateConfigRequest.md)|  | 

### Return type

[**ConfigEntry**](ConfigEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration entry updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

