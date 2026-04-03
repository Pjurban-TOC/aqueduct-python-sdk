# aqueduct_sdk.SubscriptionsApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /api/v1/webhooks/subscriptions | Create a webhook subscription
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /api/v1/webhooks/subscriptions/{subscription_id} | Delete a webhook subscription
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /api/v1/webhooks/subscriptions/{subscription_id} | Get subscription details
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /api/v1/webhooks/subscriptions | List webhook subscriptions
[**rotate_subscription_secret**](SubscriptionsApi.md#rotate_subscription_secret) | **POST** /api/v1/webhooks/subscriptions/{subscription_id}/rotate-secret | Rotate subscription signing secret
[**test_subscription**](SubscriptionsApi.md#test_subscription) | **POST** /api/v1/webhooks/subscriptions/{subscription_id}/test | Send a test event
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PUT** /api/v1/webhooks/subscriptions/{subscription_id} | Update a webhook subscription


# **create_subscription**
> CreateSubscription201Response create_subscription(create_subscription_request)

Create a webhook subscription

Creates a new webhook subscription. The subscription will receive
events matching the specified types at the provided URL. A signing
secret is generated and returned once.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_subscription201_response import CreateSubscription201Response
from aqueduct_sdk.models.create_subscription_request import CreateSubscriptionRequest
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    create_subscription_request = {"url":"https://hooks.acme.example.com/aqueduct","event_types":["dlp.alert","safety.violation"],"headers":{"X-Custom-Auth":"secret-token-123"},"description":"Production webhook for security events","max_retries":5,"timeout_sec":30,"rate_limit_rpm":60} # CreateSubscriptionRequest | 

    try:
        # Create a webhook subscription
        api_response = await api_instance.create_subscription(create_subscription_request)
        print("The response of SubscriptionsApi->create_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscription_request** | [**CreateSubscriptionRequest**](CreateSubscriptionRequest.md)|  | 

### Return type

[**CreateSubscription201Response**](CreateSubscription201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription created. The signing secret is included only in this response. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> DeleteResponse delete_subscription(subscription_id)

Delete a webhook subscription

Permanently deletes a webhook subscription. Pending deliveries are cancelled.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.delete_response import DeleteResponse
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Delete a webhook subscription
        api_response = await api_instance.delete_subscription(subscription_id)
        print("The response of SubscriptionsApi->delete_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription deleted. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(subscription_id)

Get subscription details

Returns detailed information about a specific webhook subscription.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.subscription import Subscription
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get subscription details
        api_response = await api_instance.get_subscription(subscription_id)
        print("The response of SubscriptionsApi->get_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> ListSubscriptionsResponse list_subscriptions(page_size=page_size, cursor=cursor)

List webhook subscriptions

Returns all webhook subscriptions for the authenticated tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_subscriptions_response import ListSubscriptionsResponse
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List webhook subscriptions
        api_response = await api_instance.list_subscriptions(page_size=page_size, cursor=cursor)
        print("The response of SubscriptionsApi->list_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**ListSubscriptionsResponse**](ListSubscriptionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_subscription_secret**
> RotateSecretResponse rotate_subscription_secret(subscription_id)

Rotate subscription signing secret

Generates a new signing secret for a subscription. The new secret is
returned once. Both old and new secrets are valid for a brief overlap
period to allow graceful rotation.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.rotate_secret_response import RotateSecretResponse
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Rotate subscription signing secret
        api_response = await api_instance.rotate_subscription_secret(subscription_id)
        print("The response of SubscriptionsApi->rotate_subscription_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->rotate_subscription_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**RotateSecretResponse**](RotateSecretResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Secret rotated. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_subscription**
> TestSubscriptionResponse test_subscription(subscription_id)

Send a test event

Sends a test webhook event to the subscription endpoint to verify connectivity.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.test_subscription_response import TestSubscriptionResponse
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Send a test event
        api_response = await api_instance.test_subscription(subscription_id)
        print("The response of SubscriptionsApi->test_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->test_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**TestSubscriptionResponse**](TestSubscriptionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Test result. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> Subscription update_subscription(subscription_id, update_subscription_request)

Update a webhook subscription

Replaces a webhook subscription's configuration.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.subscription import Subscription
from aqueduct_sdk.models.update_subscription_request import UpdateSubscriptionRequest
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
    api_instance = aqueduct_sdk.SubscriptionsApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
    update_subscription_request = {"url":"https://hooks.acme.example.com/v2/aqueduct","event_types":["dlp.alert","prompt.processed"],"active":true,"max_retries":10,"timeout_sec":15} # UpdateSubscriptionRequest | 

    try:
        # Update a webhook subscription
        api_response = await api_instance.update_subscription(subscription_id, update_subscription_request)
        print("The response of SubscriptionsApi->update_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **update_subscription_request** | [**UpdateSubscriptionRequest**](UpdateSubscriptionRequest.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

