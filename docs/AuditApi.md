# aqueduct_sdk.AuditApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_entry**](AuditApi.md#get_audit_log_entry) | **GET** /v1/audit/logs/{log_id} | Get a single audit log entry
[**get_audit_stats**](AuditApi.md#get_audit_stats) | **GET** /v1/audit/stats | Get audit log statistics
[**query_audit_logs**](AuditApi.md#query_audit_logs) | **GET** /v1/audit/logs | Query audit logs


# **get_audit_log_entry**
> AuditLogEntry get_audit_log_entry(log_id)

Get a single audit log entry

Returns the full audit log entry for a specific event ID, including
all request/response metadata, model info, usage, performance metrics,
DLP results, safety results, RAG context, and compliance evaluation.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.audit_log_entry import AuditLogEntry
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
    api_instance = aqueduct_sdk.AuditApi(api_client)
    log_id = 'log_id_example' # str | Audit log entry event ID.

    try:
        # Get a single audit log entry
        api_response = await api_instance.get_audit_log_entry(log_id)
        print("The response of AuditApi->get_audit_log_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->get_audit_log_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_id** | **str**| Audit log entry event ID. | 

### Return type

[**AuditLogEntry**](AuditLogEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Full audit log entry. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_stats**
> GetAuditStats200Response get_audit_stats(start_time, end_time, tenant_id=tenant_id, group_by=group_by)

Get audit log statistics

Returns aggregated statistics across audit logs for a given time range
and optional filters. Useful for compliance dashboards and SLO tracking.
Includes request counts, token usage, cost, latency percentiles, and
error rates per ISpec [arXiv:2512.17259] observability requirements.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.get_audit_stats200_response import GetAuditStats200Response
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
    api_instance = aqueduct_sdk.AuditApi(api_client)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | Start of time range (ISO 8601).
    end_time = '2013-10-20T19:20:30+01:00' # datetime | End of time range (ISO 8601).
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID. (optional)
    group_by = 'group_by_example' # str | Dimension to group statistics by. (optional)

    try:
        # Get audit log statistics
        api_response = await api_instance.get_audit_stats(start_time, end_time, tenant_id=tenant_id, group_by=group_by)
        print("The response of AuditApi->get_audit_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->get_audit_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **datetime**| Start of time range (ISO 8601). | 
 **end_time** | **datetime**| End of time range (ISO 8601). | 
 **tenant_id** | **str**| Filter by tenant ID. | [optional] 
 **group_by** | **str**| Dimension to group statistics by. | [optional] 

### Return type

[**GetAuditStats200Response**](GetAuditStats200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Aggregated audit statistics. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_audit_logs**
> AuditLogQueryResponse query_audit_logs(tenant_id=tenant_id, user_id=user_id, start_time=start_time, end_time=end_time, path=path, status_code=status_code, model_id=model_id, has_dlp_findings=has_dlp_findings, has_safety_findings=has_safety_findings, min_latency_ms=min_latency_ms, page_size=page_size, cursor=cursor)

Query audit logs

Searches and filters audit log entries with support for time ranges,
tenant filtering, model filtering, DLP/safety finding filters, and
latency thresholds. Returns paginated results with optional aggregations.
Per AEGIS [arXiv:2603.12621], every API call is logged with full
request/response metadata for compliance and observability.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.audit_log_query_response import AuditLogQueryResponse
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
    api_instance = aqueduct_sdk.AuditApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter by tenant ID. (optional)
    user_id = 'user_id_example' # str | Filter by user ID. (optional)
    start_time = '2013-10-20T19:20:30+01:00' # datetime | Start of time range (ISO 8601). (optional)
    end_time = '2013-10-20T19:20:30+01:00' # datetime | End of time range (ISO 8601). (optional)
    path = '/v1/chat/*' # str | Filter by request path (supports wildcard `*`). (optional)
    status_code = 56 # int | Filter by HTTP response status code. (optional)
    model_id = 'model_id_example' # str | Filter by model identifier. (optional)
    has_dlp_findings = True # bool | Filter to requests with DLP findings. (optional)
    has_safety_findings = True # bool | Filter to requests with safety findings. (optional)
    min_latency_ms = 56 # int | Filter to requests exceeding this latency threshold. (optional)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # Query audit logs
        api_response = await api_instance.query_audit_logs(tenant_id=tenant_id, user_id=user_id, start_time=start_time, end_time=end_time, path=path, status_code=status_code, model_id=model_id, has_dlp_findings=has_dlp_findings, has_safety_findings=has_safety_findings, min_latency_ms=min_latency_ms, page_size=page_size, cursor=cursor)
        print("The response of AuditApi->query_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditApi->query_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter by tenant ID. | [optional] 
 **user_id** | **str**| Filter by user ID. | [optional] 
 **start_time** | **datetime**| Start of time range (ISO 8601). | [optional] 
 **end_time** | **datetime**| End of time range (ISO 8601). | [optional] 
 **path** | **str**| Filter by request path (supports wildcard &#x60;*&#x60;). | [optional] 
 **status_code** | **int**| Filter by HTTP response status code. | [optional] 
 **model_id** | **str**| Filter by model identifier. | [optional] 
 **has_dlp_findings** | **bool**| Filter to requests with DLP findings. | [optional] 
 **has_safety_findings** | **bool**| Filter to requests with safety findings. | [optional] 
 **min_latency_ms** | **int**| Filter to requests exceeding this latency threshold. | [optional] 
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**AuditLogQueryResponse**](AuditLogQueryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit log query results. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

