# aqueduct_sdk.ComplianceApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compliance_evidence**](ComplianceApi.md#get_compliance_evidence) | **GET** /api/v1/compliance/evidence | List compliance evidence
[**get_compliance_gap_report**](ComplianceApi.md#get_compliance_gap_report) | **GET** /api/v1/compliance/gap-report | Get compliance gap analysis report
[**get_compliance_status**](ComplianceApi.md#get_compliance_status) | **GET** /api/v1/compliance/status | Get overall compliance status
[**get_framework_controls**](ComplianceApi.md#get_framework_controls) | **GET** /api/v1/frameworks/{frameworkID}/controls | Get controls for a compliance framework
[**list_compliance_frameworks**](ComplianceApi.md#list_compliance_frameworks) | **GET** /api/v1/frameworks | List compliance frameworks
[**run_compliance_check**](ComplianceApi.md#run_compliance_check) | **POST** /api/v1/compliance/check | Run a compliance check
[**set_compliance_tenants**](ComplianceApi.md#set_compliance_tenants) | **POST** /api/v1/compliance/tenants | Set tenants for compliance scheduler


# **get_compliance_evidence**
> EvidenceListResponse get_compliance_evidence(tenant_id=tenant_id, control_id=control_id, page_size=page_size, cursor=cursor)

List compliance evidence

Returns paginated compliance evidence records. Evidence is collected
automatically from configuration checks, audit logs, and security
scans per CISA Secure by Design (2024-2025) requirements.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.evidence_list_response import EvidenceListResponse
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Filter or scope results to a specific tenant. (optional)
    control_id = 'control_id_example' # str | Filter by control ID. (optional)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List compliance evidence
        api_response = await api_instance.get_compliance_evidence(tenant_id=tenant_id, control_id=control_id, page_size=page_size, cursor=cursor)
        print("The response of ComplianceApi->get_compliance_evidence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_evidence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Filter or scope results to a specific tenant. | [optional] 
 **control_id** | **str**| Filter by control ID. | [optional] 
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**EvidenceListResponse**](EvidenceListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compliance evidence list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_gap_report**
> GapAnalysisReport get_compliance_gap_report(framework_id, tenant_id)

Get compliance gap analysis report

Returns a gap analysis report for a specific framework and tenant,
showing which controls are met, unmet, or partial. Supports
ISpec [arXiv:2512.17259] policy evaluation workflow.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.gap_analysis_report import GapAnalysisReport
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    framework_id = 'soc2-2024' # str | Framework to analyse.
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant to evaluate.

    try:
        # Get compliance gap analysis report
        api_response = await api_instance.get_compliance_gap_report(framework_id, tenant_id)
        print("The response of ComplianceApi->get_compliance_gap_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_gap_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **framework_id** | **str**| Framework to analyse. | 
 **tenant_id** | **str**| Tenant to evaluate. | 

### Return type

[**GapAnalysisReport**](GapAnalysisReport.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gap analysis report. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_status**
> OverallComplianceStatus get_compliance_status(tenant_id)

Get overall compliance status

Returns the overall compliance posture for a tenant across all
registered frameworks, including per-framework compliance percentages.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.overall_compliance_status import OverallComplianceStatus
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant to evaluate.

    try:
        # Get overall compliance status
        api_response = await api_instance.get_compliance_status(tenant_id)
        print("The response of ComplianceApi->get_compliance_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_compliance_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant to evaluate. | 

### Return type

[**OverallComplianceStatus**](OverallComplianceStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Overall compliance status. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_framework_controls**
> ControlListResponse get_framework_controls(framework_id, tenant_id=tenant_id)

Get controls for a compliance framework

Returns all controls within a specific compliance framework, optionally
scoped to a tenant to include control assessment status.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.control_list_response import ControlListResponse
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    framework_id = 'soc2-2024' # str | Compliance framework identifier.
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Filter or scope results to a specific tenant. (optional)

    try:
        # Get controls for a compliance framework
        api_response = await api_instance.get_framework_controls(framework_id, tenant_id=tenant_id)
        print("The response of ComplianceApi->get_framework_controls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_framework_controls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **framework_id** | **str**| Compliance framework identifier. | 
 **tenant_id** | **str**| Filter or scope results to a specific tenant. | [optional] 

### Return type

[**ControlListResponse**](ControlListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Framework controls. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_frameworks**
> FrameworkListResponse list_compliance_frameworks()

List compliance frameworks

Returns all supported compliance frameworks. Aqueduct supports SOC 2,
HIPAA, FedRAMP, GDPR, and ISO 27001 per NIST AI RMF 1.0
Govern/Map/Measure/Manage functions.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.framework_list_response import FrameworkListResponse
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)

    try:
        # List compliance frameworks
        api_response = await api_instance.list_compliance_frameworks()
        print("The response of ComplianceApi->list_compliance_frameworks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_compliance_frameworks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FrameworkListResponse**](FrameworkListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compliance framework list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_compliance_check**
> CheckResult run_compliance_check(run_compliance_check_request)

Run a compliance check

Executes a compliance check for a given framework and tenant. If
`control_id` is omitted, all controls in the framework are checked.
Per AEGIS [arXiv:2603.12621], results include evidence references
for audit trail.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.check_result import CheckResult
from aqueduct_sdk.models.run_compliance_check_request import RunComplianceCheckRequest
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    run_compliance_check_request = {"framework_id":"soc2-2024","tenant_id":"tnt_acme-corp_a1b2c3","control_id":"soc2-cc6.1"} # RunComplianceCheckRequest | 

    try:
        # Run a compliance check
        api_response = await api_instance.run_compliance_check(run_compliance_check_request)
        print("The response of ComplianceApi->run_compliance_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->run_compliance_check: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_compliance_check_request** | [**RunComplianceCheckRequest**](RunComplianceCheckRequest.md)|  | 

### Return type

[**CheckResult**](CheckResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compliance check result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_compliance_tenants**
> SetTenantsResponse set_compliance_tenants(set_tenants_request)

Set tenants for compliance scheduler

Configures which tenants are included in the automated compliance
check scheduler. The scheduler runs periodic assessments for all
configured tenants.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.set_tenants_request import SetTenantsRequest
from aqueduct_sdk.models.set_tenants_response import SetTenantsResponse
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
    api_instance = aqueduct_sdk.ComplianceApi(api_client)
    set_tenants_request = {"tenant_ids":["tnt_acme-corp_a1b2c3","tnt_globex-inc_d4e5f6","tnt_initech_g7h8i9"]} # SetTenantsRequest | 

    try:
        # Set tenants for compliance scheduler
        api_response = await api_instance.set_compliance_tenants(set_tenants_request)
        print("The response of ComplianceApi->set_compliance_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->set_compliance_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_tenants_request** | [**SetTenantsRequest**](SetTenantsRequest.md)|  | 

### Return type

[**SetTenantsResponse**](SetTenantsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scheduler tenants updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

