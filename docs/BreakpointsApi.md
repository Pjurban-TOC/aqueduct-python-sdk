# aqueduct_sdk.BreakpointsApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_paused_request**](BreakpointsApi.md#approve_paused_request) | **POST** /api/v1/admin/breakpoints/paused/{id}/approve | Approve a paused request
[**create_breakpoint**](BreakpointsApi.md#create_breakpoint) | **POST** /api/v1/admin/breakpoints | Create a breakpoint
[**delete_breakpoint**](BreakpointsApi.md#delete_breakpoint) | **DELETE** /api/v1/admin/breakpoints/{id} | Delete a breakpoint
[**disable_breakpoint**](BreakpointsApi.md#disable_breakpoint) | **POST** /api/v1/admin/breakpoints/{id}/disable | Disable a breakpoint
[**enable_breakpoint**](BreakpointsApi.md#enable_breakpoint) | **POST** /api/v1/admin/breakpoints/{id}/enable | Enable a breakpoint
[**get_breakpoint**](BreakpointsApi.md#get_breakpoint) | **GET** /api/v1/admin/breakpoints/{id} | Get breakpoint details
[**get_breakpoint_history**](BreakpointsApi.md#get_breakpoint_history) | **GET** /api/v1/admin/breakpoints/{id}/history | Get breakpoint activation history
[**get_paused_request**](BreakpointsApi.md#get_paused_request) | **GET** /api/v1/admin/breakpoints/paused/{id} | Get paused request details
[**get_queue_stats**](BreakpointsApi.md#get_queue_stats) | **GET** /api/v1/admin/breakpoints/queue/stats | Get breakpoint queue statistics
[**list_breakpoints**](BreakpointsApi.md#list_breakpoints) | **GET** /api/v1/admin/breakpoints | List breakpoints
[**list_paused_requests**](BreakpointsApi.md#list_paused_requests) | **GET** /api/v1/admin/breakpoints/paused | List paused requests
[**modify_paused_request**](BreakpointsApi.md#modify_paused_request) | **POST** /api/v1/admin/breakpoints/paused/{id}/modify | Modify and approve a paused request
[**reject_paused_request**](BreakpointsApi.md#reject_paused_request) | **POST** /api/v1/admin/breakpoints/paused/{id}/reject | Reject a paused request
[**stream_breakpoint_events**](BreakpointsApi.md#stream_breakpoint_events) | **GET** /ws/admin/breakpoints | Real-time breakpoint event stream (WebSocket)
[**test_breakpoint**](BreakpointsApi.md#test_breakpoint) | **POST** /api/v1/admin/breakpoints/{id}/test | Test a breakpoint against sample fields
[**update_breakpoint**](BreakpointsApi.md#update_breakpoint) | **PUT** /api/v1/admin/breakpoints/{id} | Update a breakpoint


# **approve_paused_request**
> ReviewResultResponse approve_paused_request(id, approve_request_body=approve_request_body)

Approve a paused request

Approves a paused request, allowing it to continue through the pipeline. Requires `breakpoint:operator` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.approve_request_body import ApproveRequestBody
from aqueduct_sdk.models.review_result_response import ReviewResultResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Paused request ID.
    approve_request_body = {"notes":"Approved after confirming business justification"} # ApproveRequestBody |  (optional)

    try:
        # Approve a paused request
        api_response = await api_instance.approve_paused_request(id, approve_request_body=approve_request_body)
        print("The response of BreakpointsApi->approve_paused_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->approve_paused_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Paused request ID. | 
 **approve_request_body** | [**ApproveRequestBody**](ApproveRequestBody.md)|  | [optional] 

### Return type

[**ReviewResultResponse**](ReviewResultResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request approved. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Request has already been reviewed. |  -  |
**410** | Request has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_breakpoint**
> BreakpointResponse create_breakpoint(create_breakpoint_request)

Create a breakpoint

Creates a new request breakpoint for intercepting AI gateway requests at a specific pipeline stage. Requires `breakpoint:admin` or `system:admin`.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse
from aqueduct_sdk.models.create_breakpoint_request import CreateBreakpointRequest
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    create_breakpoint_request = {"tenant_id":"tnt_acme-corp_a1b2c3","name":"Flag large token requests","description":"Pause requests exceeding 4000 tokens for manual review","stage":"PRE_MODEL_CALL","mode":"pause","conditions":[{"field":"token_count","operator":"gt","value":4000}],"priority":"high"} # CreateBreakpointRequest | 

    try:
        # Create a breakpoint
        api_response = await api_instance.create_breakpoint(create_breakpoint_request)
        print("The response of BreakpointsApi->create_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->create_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_breakpoint_request** | [**CreateBreakpointRequest**](CreateBreakpointRequest.md)|  | 

### Return type

[**BreakpointResponse**](BreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Breakpoint created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_breakpoint**
> delete_breakpoint(id)

Delete a breakpoint

Permanently removes a breakpoint. Requires `breakpoint:admin`.

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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.

    try:
        # Delete a breakpoint
        await api_instance.delete_breakpoint(id)
    except Exception as e:
        print("Exception when calling BreakpointsApi->delete_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 

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
**204** | Breakpoint deleted. |  -  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_breakpoint**
> BreakpointResponse disable_breakpoint(id)

Disable a breakpoint

Deactivates a breakpoint without deleting it. Requires `breakpoint:admin`.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.

    try:
        # Disable a breakpoint
        api_response = await api_instance.disable_breakpoint(id)
        print("The response of BreakpointsApi->disable_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->disable_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 

### Return type

[**BreakpointResponse**](BreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Breakpoint disabled. Returns the updated breakpoint. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_breakpoint**
> BreakpointResponse enable_breakpoint(id)

Enable a breakpoint

Activates a disabled breakpoint. Requires `breakpoint:admin`.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.

    try:
        # Enable a breakpoint
        api_response = await api_instance.enable_breakpoint(id)
        print("The response of BreakpointsApi->enable_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->enable_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 

### Return type

[**BreakpointResponse**](BreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Breakpoint enabled. Returns the updated breakpoint. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_breakpoint**
> BreakpointResponse get_breakpoint(id)

Get breakpoint details

Returns details for a specific breakpoint. Requires `breakpoint:viewer` or higher.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.

    try:
        # Get breakpoint details
        api_response = await api_instance.get_breakpoint(id)
        print("The response of BreakpointsApi->get_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->get_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 

### Return type

[**BreakpointResponse**](BreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Breakpoint details. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_breakpoint_history**
> ActivationHistoryResponse get_breakpoint_history(id, limit=limit)

Get breakpoint activation history

Returns the activation history for a breakpoint. Requires `breakpoint:viewer` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.activation_history_response import ActivationHistoryResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.
    limit = 50 # int | Maximum number of history records (1-100, default 50). (optional) (default to 50)

    try:
        # Get breakpoint activation history
        api_response = await api_instance.get_breakpoint_history(id, limit=limit)
        print("The response of BreakpointsApi->get_breakpoint_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->get_breakpoint_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 
 **limit** | **int**| Maximum number of history records (1-100, default 50). | [optional] [default to 50]

### Return type

[**ActivationHistoryResponse**](ActivationHistoryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activation history. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paused_request**
> PausedRequestDetailResponse get_paused_request(id)

Get paused request details

Returns full details for a specific paused request, including the request snapshot for operator review. Requires `breakpoint:operator` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.paused_request_detail_response import PausedRequestDetailResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Paused request ID.

    try:
        # Get paused request details
        api_response = await api_instance.get_paused_request(id)
        print("The response of BreakpointsApi->get_paused_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->get_paused_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Paused request ID. | 

### Return type

[**PausedRequestDetailResponse**](PausedRequestDetailResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paused request details with full request snapshot. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_stats**
> QueueStatsResponse get_queue_stats(tenant_id=tenant_id)

Get breakpoint queue statistics

Returns aggregate statistics for the breakpoint review queue. System admins may pass `tenant_id` to view stats for a specific tenant. Requires `breakpoint:viewer` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.queue_stats_response import QueueStatsResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    tenant_id = 'tenant_id_example' # str | View stats for a specific tenant (system admin only). (optional)

    try:
        # Get breakpoint queue statistics
        api_response = await api_instance.get_queue_stats(tenant_id=tenant_id)
        print("The response of BreakpointsApi->get_queue_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->get_queue_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| View stats for a specific tenant (system admin only). | [optional] 

### Return type

[**QueueStatsResponse**](QueueStatsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Queue statistics. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_breakpoints**
> BreakpointListResponse list_breakpoints(stage=stage, mode=mode, enabled=enabled, limit=limit, cursor=cursor, all_tenants=all_tenants)

List breakpoints

Returns a paginated list of breakpoints for the caller's tenant. System admins may pass `all_tenants=true` to list across tenants. Requires `breakpoint:viewer` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_list_response import BreakpointListResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    stage = 'stage_example' # str | Filter by pipeline stage. (optional)
    mode = 'mode_example' # str | Filter by breakpoint mode. (optional)
    enabled = True # bool | Filter by enabled status. (optional)
    limit = 50 # int | Maximum number of results (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | Cursor for pagination (value from `next_cursor` in a previous response). (optional)
    all_tenants = True # bool | When `true`, list breakpoints across all tenants (system admin only). (optional)

    try:
        # List breakpoints
        api_response = await api_instance.list_breakpoints(stage=stage, mode=mode, enabled=enabled, limit=limit, cursor=cursor, all_tenants=all_tenants)
        print("The response of BreakpointsApi->list_breakpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->list_breakpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stage** | **str**| Filter by pipeline stage. | [optional] 
 **mode** | **str**| Filter by breakpoint mode. | [optional] 
 **enabled** | **bool**| Filter by enabled status. | [optional] 
 **limit** | **int**| Maximum number of results (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| Cursor for pagination (value from &#x60;next_cursor&#x60; in a previous response). | [optional] 
 **all_tenants** | **bool**| When &#x60;true&#x60;, list breakpoints across all tenants (system admin only). | [optional] 

### Return type

[**BreakpointListResponse**](BreakpointListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Breakpoint list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_paused_requests**
> PausedRequestListResponse list_paused_requests(status=status, priority=priority, stage=stage, breakpoint_id=breakpoint_id, limit=limit, cursor=cursor, all_tenants=all_tenants)

List paused requests

Returns a paginated list of requests paused by breakpoints and awaiting review. Defaults to `status=pending`. Requires `breakpoint:operator` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.paused_request_list_response import PausedRequestListResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    status = pending # str | Filter by review status. Defaults to `pending`. (optional) (default to pending)
    priority = 'priority_example' # str | Filter by priority level. (optional)
    stage = 'stage_example' # str | Filter by pipeline stage. (optional)
    breakpoint_id = 'breakpoint_id_example' # str | Filter by the breakpoint that caused the pause. (optional)
    limit = 50 # int | Maximum number of results (1-100, default 50). (optional) (default to 50)
    cursor = 'cursor_example' # str | Cursor for pagination. (optional)
    all_tenants = True # bool | When `true`, list across all tenants (system admin only). (optional)

    try:
        # List paused requests
        api_response = await api_instance.list_paused_requests(status=status, priority=priority, stage=stage, breakpoint_id=breakpoint_id, limit=limit, cursor=cursor, all_tenants=all_tenants)
        print("The response of BreakpointsApi->list_paused_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->list_paused_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by review status. Defaults to &#x60;pending&#x60;. | [optional] [default to pending]
 **priority** | **str**| Filter by priority level. | [optional] 
 **stage** | **str**| Filter by pipeline stage. | [optional] 
 **breakpoint_id** | **str**| Filter by the breakpoint that caused the pause. | [optional] 
 **limit** | **int**| Maximum number of results (1-100, default 50). | [optional] [default to 50]
 **cursor** | **str**| Cursor for pagination. | [optional] 
 **all_tenants** | **bool**| When &#x60;true&#x60;, list across all tenants (system admin only). | [optional] 

### Return type

[**PausedRequestListResponse**](PausedRequestListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paused request list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_paused_request**
> ReviewResultResponse modify_paused_request(id, modify_request_body)

Modify and approve a paused request

Applies modifications to a paused request and then approves it for continued processing. Requires `breakpoint:operator` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.modify_request_body import ModifyRequestBody
from aqueduct_sdk.models.review_result_response import ReviewResultResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Paused request ID.
    modify_request_body = {"modifications":{"model":"gpt-3.5-turbo","max_tokens":2000},"notes":"Downgraded model to reduce cost and risk"} # ModifyRequestBody | 

    try:
        # Modify and approve a paused request
        api_response = await api_instance.modify_paused_request(id, modify_request_body)
        print("The response of BreakpointsApi->modify_paused_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->modify_paused_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Paused request ID. | 
 **modify_request_body** | [**ModifyRequestBody**](ModifyRequestBody.md)|  | 

### Return type

[**ReviewResultResponse**](ReviewResultResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request modified and approved. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Request has already been reviewed. |  -  |
**410** | Request has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_paused_request**
> ReviewResultResponse reject_paused_request(id, reject_request_body)

Reject a paused request

Rejects a paused request. The original caller receives an error. A `reason` is required. Requires `breakpoint:operator` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.reject_request_body import RejectRequestBody
from aqueduct_sdk.models.review_result_response import ReviewResultResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Paused request ID.
    reject_request_body = {"reason":"Request contains unapproved PII that violates compliance policy"} # RejectRequestBody | 

    try:
        # Reject a paused request
        api_response = await api_instance.reject_paused_request(id, reject_request_body)
        print("The response of BreakpointsApi->reject_paused_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->reject_paused_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Paused request ID. | 
 **reject_request_body** | [**RejectRequestBody**](RejectRequestBody.md)|  | 

### Return type

[**ReviewResultResponse**](ReviewResultResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request rejected. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Request has already been reviewed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_breakpoint_events**
> stream_breakpoint_events(tenant_id=tenant_id)

Real-time breakpoint event stream (WebSocket)

Upgrades to a WebSocket connection for real-time breakpoint notifications.
This is a WebSocket endpoint; clients must send an HTTP `Upgrade: websocket`
request.

**Authentication / tenant identification:**
The server reads tenant and user context from request headers or query
parameters:
  - `X-Tenant-ID` header (or `tenant_id` query parameter)
  - `X-User-ID` header
  - `X-User-Scopes` header (comma-separated)

The caller must hold one of the following scopes:
`breakpoint:viewer`, `breakpoint:operator`, `breakpoint:admin`,
or `system:admin`.

**Server -> Client messages (JSON):**
```json
{
  "channel": "breakpoint:paused",
  "event": "request_paused",
  "data": {
    "request_id": "...",
    "breakpoint_id": "...",
    "breakpoint_name": "...",
    "tenant_id": "...",
    "user_id": "...",
    "stage": "PRE_MODEL_CALL",
    "priority": "high",
    "sanitized_preview": "...",
    "paused_at": "2026-03-19T12:00:00Z",
    "expires_at": "2026-03-19T12:05:00Z"
  },
  "timestamp": "2026-03-19T12:00:00Z"
}
```

**Channels:**
| Channel | Event | Description |
|---|---|---|
| `breakpoint:paused` | `request_paused` | A request was paused by a breakpoint |
| `breakpoint:reviewed` | `request_reviewed` | A paused request was approved/rejected |
| `breakpoint:expired` | `request_expired` | A paused request expired without review |
| `breakpoint:config` | `config_changed` | A breakpoint was created, updated, deleted, enabled, or disabled |

Messages are scoped to the caller's tenant. Global breakpoints
(`tenant_id: "*"`) broadcast to all connected tenants.

**Client -> Server messages (JSON):**
```json
{ "type": "ping" }
```
The server replies with `{ "type": "pong", "timestamp": "..." }`.


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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    tenant_id = 'tenant_id_example' # str | Tenant identifier. Falls back to `X-Tenant-ID` header when not provided. Required for connection to be accepted.  (optional)

    try:
        # Real-time breakpoint event stream (WebSocket)
        await api_instance.stream_breakpoint_events(tenant_id=tenant_id)
    except Exception as e:
        print("Exception when calling BreakpointsApi->stream_breakpoint_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier. Falls back to &#x60;X-Tenant-ID&#x60; header when not provided. Required for connection to be accepted.  | [optional] 

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
**400** | Tenant ID is required but was not provided. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_breakpoint**
> TestBreakpointResponse test_breakpoint(id, test_breakpoint_request)

Test a breakpoint against sample fields

Evaluates a breakpoint's conditions against the provided field map without actually triggering the breakpoint. Requires `breakpoint:viewer` or higher.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.test_breakpoint_request import TestBreakpointRequest
from aqueduct_sdk.models.test_breakpoint_response import TestBreakpointResponse
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.
    test_breakpoint_request = {"fields":{"token_count":5200,"model":"gpt-4","user_id":"usr_johndoe_abc123"}} # TestBreakpointRequest | 

    try:
        # Test a breakpoint against sample fields
        api_response = await api_instance.test_breakpoint(id, test_breakpoint_request)
        print("The response of BreakpointsApi->test_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->test_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 
 **test_breakpoint_request** | [**TestBreakpointRequest**](TestBreakpointRequest.md)|  | 

### Return type

[**TestBreakpointResponse**](TestBreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test result. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_breakpoint**
> BreakpointResponse update_breakpoint(id, update_breakpoint_request)

Update a breakpoint

Updates a breakpoint configuration. The `version` field is required for optimistic locking — it must match the current server-side version. Requires `breakpoint:admin`.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse
from aqueduct_sdk.models.update_breakpoint_request import UpdateBreakpointRequest
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
    api_instance = aqueduct_sdk.BreakpointsApi(api_client)
    id = 'id_example' # str | Breakpoint ID.
    update_breakpoint_request = {"name":"Flag very large token requests","description":"Pause requests exceeding 8000 tokens","conditions":[{"field":"token_count","operator":"gt","value":8000}],"priority":"critical","version":3} # UpdateBreakpointRequest | 

    try:
        # Update a breakpoint
        api_response = await api_instance.update_breakpoint(id, update_breakpoint_request)
        print("The response of BreakpointsApi->update_breakpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BreakpointsApi->update_breakpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Breakpoint ID. | 
 **update_breakpoint_request** | [**UpdateBreakpointRequest**](UpdateBreakpointRequest.md)|  | 

### Return type

[**BreakpointResponse**](BreakpointResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Breakpoint updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Version conflict — the breakpoint was modified since last read. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

