# aqueduct_sdk.ActivityApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_activity_events**](ActivityApi.md#batch_create_activity_events) | **POST** /admin/activity/events/batch | Batch create activity events
[**create_activity_event**](ActivityApi.md#create_activity_event) | **POST** /admin/activity/events | Create an activity event
[**export_activity_events**](ActivityApi.md#export_activity_events) | **POST** /admin/activity/export | Export activity events
[**export_activity_events_csv**](ActivityApi.md#export_activity_events_csv) | **POST** /admin/activity/export/csv | Export activity events as CSV
[**export_activity_events_json**](ActivityApi.md#export_activity_events_json) | **POST** /admin/activity/export/json | Export activity events as JSON
[**get_activity_aggregates**](ActivityApi.md#get_activity_aggregates) | **GET** /admin/activity/dashboard/aggregates | Get activity aggregates
[**get_activity_dashboard**](ActivityApi.md#get_activity_dashboard) | **GET** /admin/activity/dashboard | Get activity dashboard
[**get_activity_dashboard_summary**](ActivityApi.md#get_activity_dashboard_summary) | **GET** /admin/activity/dashboard/summary | Get dashboard summary
[**get_activity_event**](ActivityApi.md#get_activity_event) | **GET** /admin/activity/events/{event_id} | Get activity event by ID
[**get_export_status**](ActivityApi.md#get_export_status) | **GET** /admin/activity/export/status/{export_id} | Get export job status
[**get_tenant_dashboard**](ActivityApi.md#get_tenant_dashboard) | **GET** /admin/activity/dashboard/tenants/{tenant_id} | Get tenant-specific dashboard
[**list_activity_events**](ActivityApi.md#list_activity_events) | **GET** /admin/activity/events | List activity events
[**list_anomalies**](ActivityApi.md#list_anomalies) | **GET** /admin/activity/dashboard/anomalies | List detected anomalies
[**stream_admin_activity**](ActivityApi.md#stream_admin_activity) | **GET** /ws/admin/activity | Real-time activity event stream (WebSocket)


# **batch_create_activity_events**
> BatchEventResponse batch_create_activity_events(batch_event_request)

Batch create activity events

Records multiple activity events in a single request.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.batch_event_request import BatchEventRequest
from aqueduct_sdk.models.batch_event_response import BatchEventResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    batch_event_request = {"events":[{"event_id":"evt_batch001","tenant_id":"tnt_acme-corp_a1b2c3","user_id":"usr_johndoe_abc123","timestamp":"2025-01-15T14:30:00Z","action":"document.view","resource_type":"document","resource_id":"doc_abc123","outcome":"success","hash_chain":"sha256:a3f2b8c1d4e5","storage_tier":"hot"},{"event_id":"evt_batch002","tenant_id":"tnt_acme-corp_a1b2c3","user_id":"usr_janedoe_def456","timestamp":"2025-01-15T14:31:00Z","action":"auth.login","resource_type":"session","resource_id":"ses_01HQ3XYZDEF456","outcome":"success","hash_chain":"sha256:b4g3c9d2e6f7","storage_tier":"hot"}]} # BatchEventRequest | 

    try:
        # Batch create activity events
        api_response = await api_instance.batch_create_activity_events(batch_event_request)
        print("The response of ActivityApi->batch_create_activity_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->batch_create_activity_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_event_request** | [**BatchEventRequest**](BatchEventRequest.md)|  | 

### Return type

[**BatchEventResponse**](BatchEventResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_activity_event**
> SuccessResponse create_activity_event(activity_event)

Create an activity event

Records a single activity event.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.activity_event import ActivityEvent
from aqueduct_sdk.models.success_response import SuccessResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    activity_event = {"event_id":"evt_01HQ3XYZAB","tenant_id":"tnt_acme-corp_a1b2c3","user_id":"usr_johndoe_abc123","timestamp":"2025-01-15T14:30:00Z","action":"document.view","resource_type":"document","resource_id":"doc_abc123","ip_address":"192.168.1.100","user_agent":"aqueduct-sdk/1.0.0","outcome":"success","hash_chain":"sha256:a3f2b8c1d4e5","storage_tier":"hot"} # ActivityEvent | 

    try:
        # Create an activity event
        api_response = await api_instance.create_activity_event(activity_event)
        print("The response of ActivityApi->create_activity_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->create_activity_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_event** | [**ActivityEvent**](ActivityEvent.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_activity_events**
> ExportResponse export_activity_events(export_request)

Export activity events

Exports activity events matching the given filters. Format is determined
by the `format` field. Maximum 100,000 records per export.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.export_request import ExportRequest
from aqueduct_sdk.models.export_response import ExportResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    export_request = {"tenant_id":"tnt_acme-corp_a1b2c3","start":"2025-01-01T00:00:00Z","end":"2025-01-31T23:59:59Z","format":"json","action":"document.view"} # ExportRequest | 

    try:
        # Export activity events
        api_response = await api_instance.export_activity_events(export_request)
        print("The response of ActivityApi->export_activity_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->export_activity_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_request** | [**ExportRequest**](ExportRequest.md)|  | 

### Return type

[**ExportResponse**](ExportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export data. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_activity_events_csv**
> str export_activity_events_csv(export_request)

Export activity events as CSV

Exports activity events in CSV format. Maximum 100,000 records.
Columns: event_id, tenant_id, user_id, timestamp, action,
resource_type, resource_id, outcome, ip_address, user_agent.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.export_request import ExportRequest
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    export_request = {"tenant_id":"tnt_acme-corp_a1b2c3","start":"2025-01-01T00:00:00Z","end":"2025-01-31T23:59:59Z","format":"csv"} # ExportRequest | 

    try:
        # Export activity events as CSV
        api_response = await api_instance.export_activity_events_csv(export_request)
        print("The response of ActivityApi->export_activity_events_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->export_activity_events_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_request** | [**ExportRequest**](ExportRequest.md)|  | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_activity_events_json**
> ExportResponse export_activity_events_json(export_request)

Export activity events as JSON

Exports activity events in JSON format. Maximum 100,000 records.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.export_request import ExportRequest
from aqueduct_sdk.models.export_response import ExportResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    export_request = {"tenant_id":"tnt_acme-corp_a1b2c3","start":"2025-01-01T00:00:00Z","end":"2025-01-31T23:59:59Z","format":"json","user_id":"usr_johndoe_abc123"} # ExportRequest | 

    try:
        # Export activity events as JSON
        api_response = await api_instance.export_activity_events_json(export_request)
        print("The response of ActivityApi->export_activity_events_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->export_activity_events_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_request** | [**ExportRequest**](ExportRequest.md)|  | 

### Return type

[**ExportResponse**](ExportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON export. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_aggregates**
> AggregatesResponse get_activity_aggregates(tenant_id=tenant_id, start=start, end=end, window=window)

Get activity aggregates

Returns activity aggregates grouped by time window.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.aggregates_response import AggregatesResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    window = hourly # str | Aggregation window type. (optional) (default to hourly)

    try:
        # Get activity aggregates
        api_response = await api_instance.get_activity_aggregates(tenant_id=tenant_id, start=start, end=end, window=window)
        print("The response of ActivityApi->get_activity_aggregates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activity_aggregates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 
 **window** | **str**| Aggregation window type. | [optional] [default to hourly]

### Return type

[**AggregatesResponse**](AggregatesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity aggregates. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_dashboard**
> DashboardResponse get_activity_dashboard(tenant_id=tenant_id, start=start, end=end)

Get activity dashboard

Returns the main dashboard view with summary, active anomalies,
and time range context.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.dashboard_response import DashboardResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. Defaults to all tenants. (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (RFC 3339). Defaults to 24 hours ago. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (RFC 3339). Defaults to now. (optional)

    try:
        # Get activity dashboard
        api_response = await api_instance.get_activity_dashboard(tenant_id=tenant_id, start=start, end=end)
        print("The response of ActivityApi->get_activity_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activity_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. Defaults to all tenants. | [optional] 
 **start** | **datetime**| Start time (RFC 3339). Defaults to 24 hours ago. | [optional] 
 **end** | **datetime**| End time (RFC 3339). Defaults to now. | [optional] 

### Return type

[**DashboardResponse**](DashboardResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard data. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_dashboard_summary**
> DashboardSummary get_activity_dashboard_summary(tenant_id=tenant_id, start=start, end=end)

Get dashboard summary

Returns aggregated summary metrics for the dashboard.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.dashboard_summary import DashboardSummary
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get dashboard summary
        api_response = await api_instance.get_activity_dashboard_summary(tenant_id=tenant_id, start=start, end=end)
        print("The response of ActivityApi->get_activity_dashboard_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activity_dashboard_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 

### Return type

[**DashboardSummary**](DashboardSummary.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard summary. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_event**
> ActivityEvent get_activity_event(event_id)

Get activity event by ID

Returns a single activity event by its ID.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.activity_event import ActivityEvent
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    event_id = 'event_id_example' # str | Activity event identifier.

    try:
        # Get activity event by ID
        api_response = await api_instance.get_activity_event(event_id)
        print("The response of ActivityApi->get_activity_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_activity_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Activity event identifier. | 

### Return type

[**ActivityEvent**](ActivityEvent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity event. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_status**
> ExportStatusResponse get_export_status(export_id)

Get export job status

Returns the status of an asynchronous export job.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.export_status_response import ExportStatusResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    export_id = 'export_id_example' # str | Export job identifier.

    try:
        # Get export job status
        api_response = await api_instance.get_export_status(export_id)
        print("The response of ActivityApi->get_export_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_export_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Export job identifier. | 

### Return type

[**ExportStatusResponse**](ExportStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export status. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_dashboard**
> TenantDashboardResponse get_tenant_dashboard(tenant_id, start=start, end=end)

Get tenant-specific dashboard

Returns dashboard data filtered to a specific tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.tenant_dashboard_response import TenantDashboardResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get tenant-specific dashboard
        api_response = await api_instance.get_tenant_dashboard(tenant_id, start=start, end=end)
        print("The response of ActivityApi->get_tenant_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_tenant_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **start** | **datetime**|  | [optional] 
 **end** | **datetime**|  | [optional] 

### Return type

[**TenantDashboardResponse**](TenantDashboardResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant dashboard data. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activity_events**
> PaginatedEventsResponse list_activity_events(tenant_id=tenant_id, user_id=user_id, action=action, start=start, end=end, cursor=cursor, page_size=page_size)

List activity events

Returns paginated activity events with filtering. Maximum query
time range is 90 days.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.paginated_events_response import PaginatedEventsResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    tenant_id = 'tenant_id_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    action = 'action_example' # str | Filter by action (e.g., document.view, auth.login). (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (RFC 3339). (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (RFC 3339). (optional)
    cursor = 'cursor_example' # str |  (optional)
    page_size = 100 # int |  (optional) (default to 100)

    try:
        # List activity events
        api_response = await api_instance.list_activity_events(tenant_id=tenant_id, user_id=user_id, action=action, start=start, end=end, cursor=cursor, page_size=page_size)
        print("The response of ActivityApi->list_activity_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->list_activity_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **action** | **str**| Filter by action (e.g., document.view, auth.login). | [optional] 
 **start** | **datetime**| Start time (RFC 3339). | [optional] 
 **end** | **datetime**| End time (RFC 3339). | [optional] 
 **cursor** | **str**|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 100]

### Return type

[**PaginatedEventsResponse**](PaginatedEventsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated activity events. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_anomalies**
> AnomaliesResponse list_anomalies(status=status)

List detected anomalies

Returns anomalies detected by the anomaly detection engine.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.anomalies_response import AnomaliesResponse
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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    status = 'status_example' # str | Filter by anomaly status. (optional)

    try:
        # List detected anomalies
        api_response = await api_instance.list_anomalies(status=status)
        print("The response of ActivityApi->list_anomalies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->list_anomalies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by anomaly status. | [optional] 

### Return type

[**AnomaliesResponse**](AnomaliesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Anomaly list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_admin_activity**
> stream_admin_activity(token=token)

Real-time activity event stream (WebSocket)

Upgrades to a WebSocket connection for real-time activity streaming.
This is a WebSocket endpoint; clients must send an HTTP `Upgrade: websocket`
request. After the connection is established, the client subscribes to
channels by sending JSON messages.

**Authentication:**
Provide a JWT token via one of the following (checked in order):
  1. `Authorization: Bearer <token>` header
  2. `admin_session` cookie
  3. `token` query parameter

**Client -> Server messages (JSON):**
```json
{ "action": "subscribe",   "channel": "<channel_name>" }
{ "action": "unsubscribe", "channel": "<channel_name>" }
```

**Available channels:**
| Channel | Description |
|---|---|
| `activity_overview` | Platform-wide activity summary updates |
| `anomalies` | Anomaly detection alerts and resolutions |
| `tenant:{tenant_id}` | Activity updates scoped to a specific tenant |

**Server -> Client messages (JSON):**
```json
{
  "channel": "activity_overview",
  "event": "activity_update",
  "data": { ... }
}
```

**Event types:** `activity_update`, `anomaly_detected`, `anomaly_resolved`,
`subscribed`, `unsubscribed`, `error`.

Delivery target is <500 ms (AC-PLAT-043-007). Anomaly alerts are delivered
within 30 seconds (BR-PLAT-043-014).


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
    api_instance = aqueduct_sdk.ActivityApi(api_client)
    token = 'token_example' # str | JWT token for authentication. Use this when the WebSocket client cannot set an `Authorization` header (e.g., browser `new WebSocket()`).  (optional)

    try:
        # Real-time activity event stream (WebSocket)
        await api_instance.stream_admin_activity(token=token)
    except Exception as e:
        print("Exception when calling ActivityApi->stream_admin_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| JWT token for authentication. Use this when the WebSocket client cannot set an &#x60;Authorization&#x60; header (e.g., browser &#x60;new WebSocket()&#x60;).  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

