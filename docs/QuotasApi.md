# aqueduct_sdk.QuotasApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_quota_alert**](QuotasApi.md#acknowledge_quota_alert) | **POST** /api/v1/tenants/{tenant_id}/quotas/alerts/{alert_id}/acknowledge | Acknowledge a quota alert
[**get_quota_alerts**](QuotasApi.md#get_quota_alerts) | **GET** /api/v1/tenants/{tenant_id}/quotas/alerts | Get quota alerts
[**get_quota_status**](QuotasApi.md#get_quota_status) | **GET** /api/v1/tenants/{tenant_id}/quotas | Get tenant quota status
[**request_quota_increase**](QuotasApi.md#request_quota_increase) | **POST** /api/v1/tenants/{tenant_id}/quotas/increase-request | Request quota increase
[**update_quota_config**](QuotasApi.md#update_quota_config) | **PATCH** /api/v1/admin/tenants/{tenant_id}/quotas | Update tenant quota configuration


# **acknowledge_quota_alert**
> AcknowledgeQuotaAlert200Response acknowledge_quota_alert(tenant_id, alert_id)

Acknowledge a quota alert

Marks a quota alert as acknowledged. Requires `tenant:admin` for
own tenant or `system:admin`.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.acknowledge_quota_alert200_response import AcknowledgeQuotaAlert200Response
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
    api_instance = aqueduct_sdk.QuotasApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    alert_id = 'alert_id_example' # str | Alert identifier.

    try:
        # Acknowledge a quota alert
        api_response = await api_instance.acknowledge_quota_alert(tenant_id, alert_id)
        print("The response of QuotasApi->acknowledge_quota_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->acknowledge_quota_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **alert_id** | **str**| Alert identifier. | 

### Return type

[**AcknowledgeQuotaAlert200Response**](AcknowledgeQuotaAlert200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert acknowledged. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_alerts**
> QuotaAlertsResponse get_quota_alerts(tenant_id, acknowledged=acknowledged)

Get quota alerts

Returns quota alerts for a tenant. Optionally filter by acknowledged status.
Requires `tenant:admin` for own tenant or `system:admin`.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.quota_alerts_response import QuotaAlertsResponse
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
    api_instance = aqueduct_sdk.QuotasApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    acknowledged = True # bool | Filter by acknowledged status. (optional)

    try:
        # Get quota alerts
        api_response = await api_instance.get_quota_alerts(tenant_id, acknowledged=acknowledged)
        print("The response of QuotasApi->get_quota_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->get_quota_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **acknowledged** | **bool**| Filter by acknowledged status. | [optional] 

### Return type

[**QuotaAlertsResponse**](QuotaAlertsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota alerts list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_status**
> QuotaStatusResponse get_quota_status(tenant_id)

Get tenant quota status

Returns current quota usage, limits, allowed models, and enabled features
for a tenant. Users can view their own tenant's quotas; system admins
can view any tenant.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.quota_status_response import QuotaStatusResponse
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
    api_instance = aqueduct_sdk.QuotasApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # Get tenant quota status
        api_response = await api_instance.get_quota_status(tenant_id)
        print("The response of QuotasApi->get_quota_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->get_quota_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**QuotaStatusResponse**](QuotaStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota status. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_quota_increase**
> QuotaIncreaseRequestResp request_quota_increase(tenant_id, quota_increase_request_req)

Request quota increase

Submit a self-service quota increase request with business justification
(minimum 20 characters). Requires `tenant:admin` for own tenant or
`system:admin`. Returns a tracking ID and expected response time.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.quota_increase_request_req import QuotaIncreaseRequestReq
from aqueduct_sdk.models.quota_increase_request_resp import QuotaIncreaseRequestResp
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
    api_instance = aqueduct_sdk.QuotasApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    quota_increase_request_req = {"resource":"api_calls_per_hour","requested_limit":20000,"justification":"Launching new product feature that requires higher API throughput for our 50k users.","urgency":"normal"} # QuotaIncreaseRequestReq | 

    try:
        # Request quota increase
        api_response = await api_instance.request_quota_increase(tenant_id, quota_increase_request_req)
        print("The response of QuotasApi->request_quota_increase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->request_quota_increase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **quota_increase_request_req** | [**QuotaIncreaseRequestReq**](QuotaIncreaseRequestReq.md)|  | 

### Return type

[**QuotaIncreaseRequestResp**](QuotaIncreaseRequestResp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Quota increase request submitted. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota_config**
> UpdateQuotaConfigResponse update_quota_config(tenant_id, update_quota_config_request)

Update tenant quota configuration

Admin endpoint to update quota limits, allowed models, enabled features,
and temporary increases. Requires `system:admin` scope.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.update_quota_config_request import UpdateQuotaConfigRequest
from aqueduct_sdk.models.update_quota_config_response import UpdateQuotaConfigResponse
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
    api_instance = aqueduct_sdk.QuotasApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    update_quota_config_request = {"limits":{"users":500,"requests_per_month":100000,"api_calls_per_hour":10000,"storage_gb":100},"models_allowed":["gpt-4","gpt-4o","claude-sonnet-4-20250514"],"features_enabled":["conversations","dlp_scanning","rag_retrieval"]} # UpdateQuotaConfigRequest | 

    try:
        # Update tenant quota configuration
        api_response = await api_instance.update_quota_config(tenant_id, update_quota_config_request)
        print("The response of QuotasApi->update_quota_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->update_quota_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **update_quota_config_request** | [**UpdateQuotaConfigRequest**](UpdateQuotaConfigRequest.md)|  | 

### Return type

[**UpdateQuotaConfigResponse**](UpdateQuotaConfigResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quota configuration updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

