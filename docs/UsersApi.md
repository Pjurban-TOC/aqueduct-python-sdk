# aqueduct_sdk.UsersApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_theme_preference**](UsersApi.md#get_user_theme_preference) | **GET** /api/v1/users/{userID}/preferences/theme | Get user theme preference
[**set_user_theme_preference**](UsersApi.md#set_user_theme_preference) | **PUT** /api/v1/users/{userID}/preferences/theme | Set user theme preference
[**stream_user_theme_preference**](UsersApi.md#stream_user_theme_preference) | **GET** /api/v1/users/{userID}/preferences/theme/sse | Stream theme preference updates via SSE


# **get_user_theme_preference**
> ThemePreferenceResponse get_user_theme_preference(user_id)

Get user theme preference

Returns the theme preference for a user, including mode (light/dark/auto),
accessibility settings (reduced motion, high contrast), and typography
scale per WCAG 2.2 (2024) requirements.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.theme_preference_response import ThemePreferenceResponse
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
    api_instance = aqueduct_sdk.UsersApi(api_client)
    user_id = 'usr_admin_xyz789' # str | User identifier.

    try:
        # Get user theme preference
        api_response = await api_instance.get_user_theme_preference(user_id)
        print("The response of UsersApi->get_user_theme_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_theme_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User identifier. | 

### Return type

[**ThemePreferenceResponse**](ThemePreferenceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User theme preference. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_theme_preference**
> ThemePreferenceResponse set_user_theme_preference(user_id, set_theme_preference_request)

Set user theme preference

Updates the theme preference for a user. Changes are propagated
to all connected devices via the SSE endpoint for cross-device
synchronization.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.set_theme_preference_request import SetThemePreferenceRequest
from aqueduct_sdk.models.theme_preference_response import ThemePreferenceResponse
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
    api_instance = aqueduct_sdk.UsersApi(api_client)
    user_id = 'usr_admin_xyz789' # str | User identifier.
    set_theme_preference_request = {"mode":"dark","reduced_motion":true,"system_high_contrast":false,"typography_scale":1.25} # SetThemePreferenceRequest | 

    try:
        # Set user theme preference
        api_response = await api_instance.set_user_theme_preference(user_id, set_theme_preference_request)
        print("The response of UsersApi->set_user_theme_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->set_user_theme_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User identifier. | 
 **set_theme_preference_request** | [**SetThemePreferenceRequest**](SetThemePreferenceRequest.md)|  | 

### Return type

[**ThemePreferenceResponse**](ThemePreferenceResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme preference updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_user_theme_preference**
> str stream_user_theme_preference(user_id, device_id, tenant_id=tenant_id)

Stream theme preference updates via SSE

Opens a Server-Sent Events (SSE) connection for real-time cross-device
theme synchronization. When a user updates their theme on one device,
all other connected devices receive the update immediately.

**Event format:**
```
event: theme-update
data: {"mode":"dark","reduced_motion":true,...}
```


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
    api_instance = aqueduct_sdk.UsersApi(api_client)
    user_id = 'usr_admin_xyz789' # str | User identifier.
    device_id = 'device_macbook_abc123' # str | Unique device identifier to deduplicate update sources.
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant context for the SSE connection. (optional)

    try:
        # Stream theme preference updates via SSE
        api_response = await api_instance.stream_user_theme_preference(user_id, device_id, tenant_id=tenant_id)
        print("The response of UsersApi->stream_user_theme_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->stream_user_theme_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User identifier. | 
 **device_id** | **str**| Unique device identifier to deduplicate update sources. | 
 **tenant_id** | **str**| Tenant context for the SSE connection. | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream of theme preference updates. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

