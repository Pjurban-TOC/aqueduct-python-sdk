# aqueduct_sdk.AssetPerformanceApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_performance_alert**](AssetPerformanceApi.md#acknowledge_performance_alert) | **PUT** /api/v1/admin/assets/alerts/{alert_id}/acknowledge | Acknowledge a performance alert
[**get_asset_time_series**](AssetPerformanceApi.md#get_asset_time_series) | **GET** /api/v1/admin/assets/timeseries | Get asset metric time series
[**get_cache_hit_rate**](AssetPerformanceApi.md#get_cache_hit_rate) | **GET** /api/v1/admin/assets/cache-hit-rate | Get cache hit rate statistics
[**get_cdn_latency**](AssetPerformanceApi.md#get_cdn_latency) | **GET** /api/v1/admin/assets/cdn-latency | Get CDN latency statistics
[**get_web_vitals_report**](AssetPerformanceApi.md#get_web_vitals_report) | **GET** /api/v1/admin/assets/web-vitals-report | Get Web Vitals report
[**ingest_asset_metrics**](AssetPerformanceApi.md#ingest_asset_metrics) | **POST** /api/v1/metrics/assets | Ingest asset performance metrics
[**list_alert_thresholds**](AssetPerformanceApi.md#list_alert_thresholds) | **GET** /api/v1/admin/assets/thresholds | List alert thresholds
[**list_performance_alerts**](AssetPerformanceApi.md#list_performance_alerts) | **GET** /api/v1/admin/assets/alerts | List performance alerts
[**set_alert_threshold**](AssetPerformanceApi.md#set_alert_threshold) | **PUT** /api/v1/admin/assets/thresholds/{metric} | Set alert threshold for a metric


# **acknowledge_performance_alert**
> AcknowledgePerformanceAlert200Response acknowledge_performance_alert(alert_id, acknowledge_alert_request)

Acknowledge a performance alert

Marks a performance alert as acknowledged with an optional note.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.acknowledge_alert_request import AcknowledgeAlertRequest
from aqueduct_sdk.models.acknowledge_performance_alert200_response import AcknowledgePerformanceAlert200Response
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    alert_id = 'alert_id_example' # str | Alert identifier.
    acknowledge_alert_request = {"acknowledged_by":"usr_admin_xyz789","note":"Investigating CDN configuration in IAD region."} # AcknowledgeAlertRequest | 

    try:
        # Acknowledge a performance alert
        api_response = await api_instance.acknowledge_performance_alert(alert_id, acknowledge_alert_request)
        print("The response of AssetPerformanceApi->acknowledge_performance_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->acknowledge_performance_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**| Alert identifier. | 
 **acknowledge_alert_request** | [**AcknowledgeAlertRequest**](AcknowledgeAlertRequest.md)|  | 

### Return type

[**AcknowledgePerformanceAlert200Response**](AcknowledgePerformanceAlert200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert acknowledged. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_time_series**
> AssetTimeSeries get_asset_time_series(tenant_id=tenant_id, metric_type=metric_type, granularity=granularity)

Get asset metric time series

Returns time series data points for a specified asset metric type and granularity.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.asset_time_series import AssetTimeSeries
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)
    metric_type = 'load_time' # str | Metric type to chart. (optional) (default to 'load_time')
    granularity = hour # str | Time bucket granularity. (optional) (default to hour)

    try:
        # Get asset metric time series
        api_response = await api_instance.get_asset_time_series(tenant_id=tenant_id, metric_type=metric_type, granularity=granularity)
        print("The response of AssetPerformanceApi->get_asset_time_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->get_asset_time_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 
 **metric_type** | **str**| Metric type to chart. | [optional] [default to &#39;load_time&#39;]
 **granularity** | **str**| Time bucket granularity. | [optional] [default to hour]

### Return type

[**AssetTimeSeries**](AssetTimeSeries.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time series data. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cache_hit_rate**
> CacheHitRateResponse get_cache_hit_rate(tenant_id=tenant_id)

Get cache hit rate statistics

Returns cache hit rate statistics broken down by asset type and CDN PoP.
Target: >99% for returning users (AC-UI-045-014).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.cache_hit_rate_response import CacheHitRateResponse
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)

    try:
        # Get cache hit rate statistics
        api_response = await api_instance.get_cache_hit_rate(tenant_id=tenant_id)
        print("The response of AssetPerformanceApi->get_cache_hit_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->get_cache_hit_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 

### Return type

[**CacheHitRateResponse**](CacheHitRateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cache hit rate statistics. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_latency**
> CdnLatencyResponse get_cdn_latency(tenant_id=tenant_id, cdn_pop=cdn_pop)

Get CDN latency statistics

Returns CDN latency percentile statistics (P50-P99) broken down by PoP
and asset type. Target: P95 <50ms (AC-UI-045-011).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.cdn_latency_response import CdnLatencyResponse
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)
    cdn_pop = 'cdn_pop_example' # str | Filter to a specific CDN point of presence. (optional)

    try:
        # Get CDN latency statistics
        api_response = await api_instance.get_cdn_latency(tenant_id=tenant_id, cdn_pop=cdn_pop)
        print("The response of AssetPerformanceApi->get_cdn_latency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->get_cdn_latency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 
 **cdn_pop** | **str**| Filter to a specific CDN point of presence. | [optional] 

### Return type

[**CdnLatencyResponse**](CdnLatencyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CDN latency statistics. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_vitals_report**
> WebVitalsReport get_web_vitals_report(tenant_id=tenant_id)

Get Web Vitals report

Returns a comprehensive Web Vitals report including FCP, LCP, FID, CLS,
TTFB, INP, and TTI with ratings and target compliance (AC-UI-045-020).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.web_vitals_report import WebVitalsReport
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)

    try:
        # Get Web Vitals report
        api_response = await api_instance.get_web_vitals_report(tenant_id=tenant_id)
        print("The response of AssetPerformanceApi->get_web_vitals_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->get_web_vitals_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 

### Return type

[**WebVitalsReport**](WebVitalsReport.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web Vitals report. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ingest_asset_metrics**
> IngestMetricsResponse ingest_asset_metrics(asset_metric_batch)

Ingest asset performance metrics

Accepts a batch of frontend asset performance metrics for storage and analysis.
Returns any triggered alerts based on configured thresholds (AC-UI-045-019).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.asset_metric_batch import AssetMetricBatch
from aqueduct_sdk.models.ingest_metrics_response import IngestMetricsResponse
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    asset_metric_batch = {"session_id":"ses_01HQ3XYZABC123","tenant_id":"tnt_acme-corp_a1b2c3","user_id":"usr_johndoe_abc123","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)","page_url":"https://app.acme.example.com/dashboard","metrics":[{"id":"metric_001","asset_url":"https://cdn.acme.example.com/app.js","type":"script","size_bytes":150000,"transfer_bytes":45000,"load_time_ms":120.5,"ttfb_ms":45,"cache_hit":true,"cdn_pop":"iad-1"}],"timestamp":"2025-01-15T14:30:00Z","connection_type":"4g","rtt_ms":50} # AssetMetricBatch | 

    try:
        # Ingest asset performance metrics
        api_response = await api_instance.ingest_asset_metrics(asset_metric_batch)
        print("The response of AssetPerformanceApi->ingest_asset_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->ingest_asset_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_metric_batch** | [**AssetMetricBatch**](AssetMetricBatch.md)|  | 

### Return type

[**IngestMetricsResponse**](IngestMetricsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics ingested successfully. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**413** | Request body exceeds maximum size (ERR-API-001-013). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_thresholds**
> List[AlertThreshold] list_alert_thresholds(tenant_id=tenant_id)

List alert thresholds

Returns all configured alert thresholds for performance metrics.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.alert_threshold import AlertThreshold
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)

    try:
        # List alert thresholds
        api_response = await api_instance.list_alert_thresholds(tenant_id=tenant_id)
        print("The response of AssetPerformanceApi->list_alert_thresholds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->list_alert_thresholds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 

### Return type

[**List[AlertThreshold]**](AlertThreshold.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert thresholds. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_performance_alerts**
> ListAlertsResponse list_performance_alerts(tenant_id=tenant_id, status=status)

List performance alerts

Returns performance alerts, optionally filtered by status.
Alerts are triggered when metrics exceed configured thresholds (AC-UI-045-021).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_alerts_response import ListAlertsResponse
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    tenant_id = 'tenant_id_example' # str | Filter to a specific tenant. (optional)
    status = 'status_example' # str | Filter by alert status. (optional)

    try:
        # List performance alerts
        api_response = await api_instance.list_performance_alerts(tenant_id=tenant_id, status=status)
        print("The response of AssetPerformanceApi->list_performance_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->list_performance_alerts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter to a specific tenant. | [optional] 
 **status** | **str**| Filter by alert status. | [optional] 

### Return type

[**ListAlertsResponse**](ListAlertsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Performance alerts. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alert_threshold**
> SetAlertThreshold200Response set_alert_threshold(metric, alert_threshold)

Set alert threshold for a metric

Creates or updates the alert threshold configuration for a specific metric.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.alert_threshold import AlertThreshold
from aqueduct_sdk.models.set_alert_threshold200_response import SetAlertThreshold200Response
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
    api_instance = aqueduct_sdk.AssetPerformanceApi(api_client)
    metric = 'metric_example' # str | Metric name (FCP, LCP, FID, CLS, TTFB, INP, TTI).
    alert_threshold = {"metric_name":"LCP","warning_threshold":2500,"critical_threshold":4000,"min_affected_pct":10,"enabled":true,"tenant_id":"tnt_acme-corp_a1b2c3"} # AlertThreshold | 

    try:
        # Set alert threshold for a metric
        api_response = await api_instance.set_alert_threshold(metric, alert_threshold)
        print("The response of AssetPerformanceApi->set_alert_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetPerformanceApi->set_alert_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| Metric name (FCP, LCP, FID, CLS, TTFB, INP, TTI). | 
 **alert_threshold** | [**AlertThreshold**](AlertThreshold.md)|  | 

### Return type

[**SetAlertThreshold200Response**](SetAlertThreshold200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threshold set. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

