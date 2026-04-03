# aqueduct_sdk.HealthApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_liveness**](HealthApi.md#get_liveness) | **GET** /healthz | Liveness probe
[**get_readiness**](HealthApi.md#get_readiness) | **GET** /readyz | Readiness probe


# **get_liveness**
> HealthResponse get_liveness()

Liveness probe

Returns 200 if the service process is running. Used by Kubernetes liveness probes.

### Example


```python
import aqueduct_sdk
from aqueduct_sdk.models.health_response import HealthResponse
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)


# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.HealthApi(api_client)

    try:
        # Liveness probe
        api_response = await api_instance.get_liveness()
        print("The response of HealthApi->get_liveness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_liveness: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is alive. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**503** | Service unavailable due to circuit breaker open (ERR-API-001-011). Includes &#x60;Retry-After&#x60; header.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_readiness**
> ReadinessResponse get_readiness()

Readiness probe

Returns 200 if the service and all dependencies are ready to accept traffic. Used by Kubernetes readiness probes.

### Example


```python
import aqueduct_sdk
from aqueduct_sdk.models.readiness_response import ReadinessResponse
from aqueduct_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.aqueduct.io:443
# See configuration.py for a list of all supported configuration parameters.
configuration = aqueduct_sdk.Configuration(
    host = "https://api.aqueduct.io:443"
)


# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.HealthApi(api_client)

    try:
        # Readiness probe
        api_response = await api_instance.get_readiness()
        print("The response of HealthApi->get_readiness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->get_readiness: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReadinessResponse**](ReadinessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is ready. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**503** | Service unavailable due to circuit breaker open (ERR-API-001-011). Includes &#x60;Retry-After&#x60; header.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

