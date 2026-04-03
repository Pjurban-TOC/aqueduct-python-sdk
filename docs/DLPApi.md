# aqueduct_sdk.DLPApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dlp_policy**](DLPApi.md#create_dlp_policy) | **POST** /v1/dlp/policies | Create a DLP policy
[**deidentify_content**](DLPApi.md#deidentify_content) | **POST** /v1/dlp/deidentify | De-identify content
[**delete_dlp_policy**](DLPApi.md#delete_dlp_policy) | **DELETE** /v1/dlp/policies/{policy_id} | Delete a DLP policy
[**get_dlp_policy**](DLPApi.md#get_dlp_policy) | **GET** /v1/dlp/policies/{policy_id} | Get DLP policy
[**list_dlp_policies**](DLPApi.md#list_dlp_policies) | **GET** /v1/dlp/policies | List DLP policies
[**scan_content**](DLPApi.md#scan_content) | **POST** /v1/dlp/scan | Scan content for PII
[**update_dlp_policy**](DLPApi.md#update_dlp_policy) | **PUT** /v1/dlp/policies/{policy_id} | Update a DLP policy


# **create_dlp_policy**
> DLPPolicy create_dlp_policy(create_dlp_policy_request)

Create a DLP policy

Creates a new DLP enforcement policy with rules for specific info types.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_dlp_policy_request import CreateDLPPolicyRequest
from aqueduct_sdk.models.dlp_policy import DLPPolicy
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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    create_dlp_policy_request = {"name":"PCI-DSS Credit Card Protection","enabled":true,"scope":"both","rules":[{"info_type":"CREDIT_CARD","action":"redact","min_score":0.8},{"info_type":"US_SSN","action":"block","min_score":0.9}],"applies_to_models":["gpt-4o"]} # CreateDLPPolicyRequest | 

    try:
        # Create a DLP policy
        api_response = await api_instance.create_dlp_policy(create_dlp_policy_request)
        print("The response of DLPApi->create_dlp_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->create_dlp_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dlp_policy_request** | [**CreateDLPPolicyRequest**](CreateDLPPolicyRequest.md)|  | 

### Return type

[**DLPPolicy**](DLPPolicy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Policy created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deidentify_content**
> DLPDeidentifyResponse deidentify_content(dlp_deidentify_request)

De-identify content

Removes or transforms PII in content according to the specified
de-identification configuration. Supports per-info-type operators
(redact, replace, mask, hash, encrypt, tokenize).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.dlp_deidentify_request import DLPDeidentifyRequest
from aqueduct_sdk.models.dlp_deidentify_response import DLPDeidentifyResponse
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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    dlp_deidentify_request = {"content":"Contact john.doe@acme.com for details. SSN is 123-45-6789.","deidentify_config":{"default_operator":{"type":"redact"},"info_type_operators":{"EMAIL_ADDRESS":{"type":"replace","replacement":"[EMAIL]"},"US_SSN":{"type":"mask","masking_char":"*","chars_to_mask":5}}},"content_type":"prompt"} # DLPDeidentifyRequest | 

    try:
        # De-identify content
        api_response = await api_instance.deidentify_content(dlp_deidentify_request)
        print("The response of DLPApi->deidentify_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->deidentify_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dlp_deidentify_request** | [**DLPDeidentifyRequest**](DLPDeidentifyRequest.md)|  | 

### Return type

[**DLPDeidentifyResponse**](DLPDeidentifyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | De-identified content. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dlp_policy**
> delete_dlp_policy(policy_id)

Delete a DLP policy

Permanently removes a DLP policy.

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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Delete a DLP policy
        await api_instance.delete_dlp_policy(policy_id)
    except Exception as e:
        print("Exception when calling DLPApi->delete_dlp_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

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
**204** | Policy deleted. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dlp_policy**
> DLPPolicy get_dlp_policy(policy_id)

Get DLP policy

Returns details for a specific DLP policy.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.dlp_policy import DLPPolicy
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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Get DLP policy
        api_response = await api_instance.get_dlp_policy(policy_id)
        print("The response of DLPApi->get_dlp_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->get_dlp_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

[**DLPPolicy**](DLPPolicy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dlp_policies**
> ListDLPPolicies200Response list_dlp_policies()

List DLP policies

Returns all DLP policies for the authenticated tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_dlp_policies200_response import ListDLPPolicies200Response
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
    api_instance = aqueduct_sdk.DLPApi(api_client)

    try:
        # List DLP policies
        api_response = await api_instance.list_dlp_policies()
        print("The response of DLPApi->list_dlp_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->list_dlp_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDLPPolicies200Response**](ListDLPPolicies200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_content**
> DLPScanResponse scan_content(dlp_scan_request)

Scan content for PII

Scans content for PII and sensitive data. Supports bidirectional scanning
(prompts AND responses). Returns findings with confidence scores and
locations. Per PII-Scope [arXiv:2410.06704], scanning both directions
is mandatory as existing evaluations underestimate leakage by 5x.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.dlp_scan_request import DLPScanRequest
from aqueduct_sdk.models.dlp_scan_response import DLPScanResponse
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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    dlp_scan_request = {"content":"Please send the invoice to john.doe@acme.com at 123 Main St, SSN 123-45-6789.","content_type":"prompt","score_threshold":0.7} # DLPScanRequest | 

    try:
        # Scan content for PII
        api_response = await api_instance.scan_content(dlp_scan_request)
        print("The response of DLPApi->scan_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->scan_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dlp_scan_request** | [**DLPScanRequest**](DLPScanRequest.md)|  | 

### Return type

[**DLPScanResponse**](DLPScanResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scan results. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dlp_policy**
> DLPPolicy update_dlp_policy(policy_id, create_dlp_policy_request)

Update a DLP policy

Replaces a DLP policy configuration.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_dlp_policy_request import CreateDLPPolicyRequest
from aqueduct_sdk.models.dlp_policy import DLPPolicy
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
    api_instance = aqueduct_sdk.DLPApi(api_client)
    policy_id = 'policy_id_example' # str | 
    create_dlp_policy_request = {"name":"Updated PCI-DSS Protection","enabled":true,"scope":"both","rules":[{"info_type":"CREDIT_CARD","action":"redact","min_score":0.85},{"info_type":"US_SSN","action":"block","min_score":0.9},{"info_type":"EMAIL_ADDRESS","action":"mask","min_score":0.8}],"applies_to_models":["gpt-4o","claude-sonnet-4-20250514"]} # CreateDLPPolicyRequest | 

    try:
        # Update a DLP policy
        api_response = await api_instance.update_dlp_policy(policy_id, create_dlp_policy_request)
        print("The response of DLPApi->update_dlp_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DLPApi->update_dlp_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **create_dlp_policy_request** | [**CreateDLPPolicyRequest**](CreateDLPPolicyRequest.md)|  | 

### Return type

[**DLPPolicy**](DLPPolicy.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

