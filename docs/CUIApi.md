# aqueduct_sdk.CUIApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_cui_marking**](CUIApi.md#apply_cui_marking) | **POST** /api/v1/cui/markings | Apply a CUI marking
[**get_cui_marking**](CUIApi.md#get_cui_marking) | **GET** /api/v1/cui/markings/{resourceID} | Get a CUI marking
[**list_cui_categories**](CUIApi.md#list_cui_categories) | **GET** /api/v1/cui/categories | List CUI categories
[**list_cui_markings**](CUIApi.md#list_cui_markings) | **GET** /api/v1/cui/markings | List CUI markings for tenant
[**list_dissemination_controls**](CUIApi.md#list_dissemination_controls) | **GET** /api/v1/cui/dissemination-controls | List dissemination controls
[**remove_cui_marking**](CUIApi.md#remove_cui_marking) | **DELETE** /api/v1/cui/markings/{resourceID} | Remove a CUI marking (decontrol)
[**update_cui_marking**](CUIApi.md#update_cui_marking) | **PUT** /api/v1/cui/markings/{resourceID} | Update a CUI marking


# **apply_cui_marking**
> StoredMarking apply_cui_marking(apply_marking_request)

Apply a CUI marking

Applies a CUI marking to a data object. Validates categories against
the NARA registry, enforces dissemination control rules (NOFORN/REL TO
mutual exclusion), and rejects retired FOUO markings.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.apply_marking_request import ApplyMarkingRequest
from aqueduct_sdk.models.stored_marking import StoredMarking
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
    api_instance = aqueduct_sdk.CUIApi(api_client)
    apply_marking_request = aqueduct_sdk.ApplyMarkingRequest() # ApplyMarkingRequest | 

    try:
        # Apply a CUI marking
        api_response = await api_instance.apply_cui_marking(apply_marking_request)
        print("The response of CUIApi->apply_cui_marking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->apply_cui_marking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_marking_request** | [**ApplyMarkingRequest**](ApplyMarkingRequest.md)|  | 

### Return type

[**StoredMarking**](StoredMarking.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Marking applied. |  -  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cui_marking**
> StoredMarking get_cui_marking(resource_id)

Get a CUI marking

Retrieves the CUI marking for a specific data object.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.stored_marking import StoredMarking
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
    api_instance = aqueduct_sdk.CUIApi(api_client)
    resource_id = 'resource_id_example' # str | 

    try:
        # Get a CUI marking
        api_response = await api_instance.get_cui_marking(resource_id)
        print("The response of CUIApi->get_cui_marking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->get_cui_marking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**|  | 

### Return type

[**StoredMarking**](StoredMarking.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marking found. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cui_categories**
> ListCategoriesResponse list_cui_categories()

List CUI categories

Returns all CUI categories from the NARA registry.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_categories_response import ListCategoriesResponse
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
    api_instance = aqueduct_sdk.CUIApi(api_client)

    try:
        # List CUI categories
        api_response = await api_instance.list_cui_categories()
        print("The response of CUIApi->list_cui_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->list_cui_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CUI category list. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cui_markings**
> ListMarkingsResponse list_cui_markings()

List CUI markings for tenant

Returns all CUI markings for the authenticated tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_markings_response import ListMarkingsResponse
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
    api_instance = aqueduct_sdk.CUIApi(api_client)

    try:
        # List CUI markings for tenant
        api_response = await api_instance.list_cui_markings()
        print("The response of CUIApi->list_cui_markings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->list_cui_markings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListMarkingsResponse**](ListMarkingsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marking list. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dissemination_controls**
> ListDisseminationControlsResponse list_dissemination_controls()

List dissemination controls

Returns all CUI dissemination control types including legacy markers.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_dissemination_controls_response import ListDisseminationControlsResponse
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
    api_instance = aqueduct_sdk.CUIApi(api_client)

    try:
        # List dissemination controls
        api_response = await api_instance.list_dissemination_controls()
        print("The response of CUIApi->list_dissemination_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->list_dissemination_controls: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDisseminationControlsResponse**](ListDisseminationControlsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dissemination control list. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_cui_marking**
> RemoveCUIMarking200Response remove_cui_marking(resource_id)

Remove a CUI marking (decontrol)

Removes a CUI marking from a data object. This is a decontrol
action per 32 CFR Part 2002. Produces a high-severity audit event.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.remove_cui_marking200_response import RemoveCUIMarking200Response
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
    api_instance = aqueduct_sdk.CUIApi(api_client)
    resource_id = 'resource_id_example' # str | 

    try:
        # Remove a CUI marking (decontrol)
        api_response = await api_instance.remove_cui_marking(resource_id)
        print("The response of CUIApi->remove_cui_marking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->remove_cui_marking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**|  | 

### Return type

[**RemoveCUIMarking200Response**](RemoveCUIMarking200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marking removed. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cui_marking**
> StoredMarking update_cui_marking(resource_id, apply_marking_request)

Update a CUI marking

Updates the CUI marking on a data object. Detects reclassification
(category changes) vs. control-only updates for audit purposes.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.apply_marking_request import ApplyMarkingRequest
from aqueduct_sdk.models.stored_marking import StoredMarking
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
    api_instance = aqueduct_sdk.CUIApi(api_client)
    resource_id = 'resource_id_example' # str | 
    apply_marking_request = aqueduct_sdk.ApplyMarkingRequest() # ApplyMarkingRequest | 

    try:
        # Update a CUI marking
        api_response = await api_instance.update_cui_marking(resource_id, apply_marking_request)
        print("The response of CUIApi->update_cui_marking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CUIApi->update_cui_marking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**|  | 
 **apply_marking_request** | [**ApplyMarkingRequest**](ApplyMarkingRequest.md)|  | 

### Return type

[**StoredMarking**](StoredMarking.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Marking updated. |  -  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

