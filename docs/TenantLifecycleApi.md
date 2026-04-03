# aqueduct_sdk.TenantLifecycleApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_deletion**](TenantLifecycleApi.md#approve_deletion) | **POST** /api/v1/admin/tenants/{tenant_id}/deletion-request/{request_id}/approve | Approve a tenant deletion request
[**create_deletion_request**](TenantLifecycleApi.md#create_deletion_request) | **POST** /api/v1/tenants/{tenant_id}/deletion-request | Create a tenant deletion request
[**download_tenant_export**](TenantLifecycleApi.md#download_tenant_export) | **GET** /api/v1/tenants/{tenant_id}/export/{export_id} | Download tenant data export
[**get_deletion_status**](TenantLifecycleApi.md#get_deletion_status) | **GET** /api/v1/tenants/{tenant_id}/deletion-status | Get tenant deletion status
[**reactivate_tenant**](TenantLifecycleApi.md#reactivate_tenant) | **POST** /api/v1/admin/tenants/{tenant_id}/reactivate | Reactivate a suspended tenant
[**suspend_tenant**](TenantLifecycleApi.md#suspend_tenant) | **POST** /api/v1/admin/tenants/{tenant_id}/suspend | Suspend a tenant


# **approve_deletion**
> ApproveDeletionResponse approve_deletion(tenant_id, request_id, approve_deletion_request)

Approve a tenant deletion request

Approves a pending deletion request. Enterprise and government tenants
require multiple approvals. The `approval_confirmation` field must
match `APPROVE DELETE {tenant_name}`. When all required approvals are
collected, the deletion workflow proceeds automatically.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.approve_deletion_request import ApproveDeletionRequest
from aqueduct_sdk.models.approve_deletion_response import ApproveDeletionResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    request_id = 'delreq_01HQ3XYZABC123' # str | Deletion request identifier.
    approve_deletion_request = {"approval_confirmation":"APPROVE DELETE Acme Corp"} # ApproveDeletionRequest | 

    try:
        # Approve a tenant deletion request
        api_response = await api_instance.approve_deletion(tenant_id, request_id, approve_deletion_request)
        print("The response of TenantLifecycleApi->approve_deletion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->approve_deletion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **request_id** | **str**| Deletion request identifier. | 
 **approve_deletion_request** | [**ApproveDeletionRequest**](ApproveDeletionRequest.md)|  | 

### Return type

[**ApproveDeletionResponse**](ApproveDeletionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deletion approval recorded. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_deletion_request**
> DeletionRequestResponse create_deletion_request(tenant_id, deletion_request_request)

Create a tenant deletion request

Initiates the tenant deletion workflow per GDPR Art. 17 right to erasure.
Enterprise and government tier tenants require multi-party approval before
deletion proceeds. The `confirmation` field must match `DELETE {tenant_name}`
to prevent accidental deletion. If `export_data` is true, a data export
is generated before soft-delete begins.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.deletion_request_request import DeletionRequestRequest
from aqueduct_sdk.models.deletion_request_response import DeletionRequestResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    deletion_request_request = {"reason":"customer_request","details":"Company is migrating to a different platform.","confirmation":"DELETE Acme Corp","export_data":true} # DeletionRequestRequest | 

    try:
        # Create a tenant deletion request
        api_response = await api_instance.create_deletion_request(tenant_id, deletion_request_request)
        print("The response of TenantLifecycleApi->create_deletion_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->create_deletion_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **deletion_request_request** | [**DeletionRequestRequest**](DeletionRequestRequest.md)|  | 

### Return type

[**DeletionRequestResponse**](DeletionRequestResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deletion request created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_tenant_export**
> ExportDownloadResponse download_tenant_export(tenant_id, export_id)

Download tenant data export

Returns metadata and a signed download URL for a tenant data export.
Exports include all tenant data, configuration, and audit logs per
GDPR Art. 20 data portability requirements.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.export_download_response import ExportDownloadResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    export_id = 'export_01HQ3XYZABC123' # str | Export identifier.

    try:
        # Download tenant data export
        api_response = await api_instance.download_tenant_export(tenant_id, export_id)
        print("The response of TenantLifecycleApi->download_tenant_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->download_tenant_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **export_id** | **str**| Export identifier. | 

### Return type

[**ExportDownloadResponse**](ExportDownloadResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export download metadata. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**410** | Resource no longer available (ERR-API-001-015). Returned by the versioning middleware when a sunsetted endpoint is accessed (OWASP API9:2023), or when a resource has been permanently removed.  |  * API-Version -  <br>  * Deprecation -  <br>  * Sunset -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deletion_status**
> DeletionStatusResponse get_deletion_status(tenant_id)

Get tenant deletion status

Returns the current status of any pending or completed deletion request
for a tenant, including approval progress, timeline, and export status.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.deletion_status_response import DeletionStatusResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # Get tenant deletion status
        api_response = await api_instance.get_deletion_status(tenant_id)
        print("The response of TenantLifecycleApi->get_deletion_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->get_deletion_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**DeletionStatusResponse**](DeletionStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deletion status. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_tenant**
> ReactivateTenantResponse reactivate_tenant(tenant_id, reactivate_tenant_request)

Reactivate a suspended tenant

Reactivates a previously suspended tenant. The tenant regains full
access immediately. Optionally waives any outstanding balance.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.reactivate_tenant_request import ReactivateTenantRequest
from aqueduct_sdk.models.reactivate_tenant_response import ReactivateTenantResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    reactivate_tenant_request = {"reason":"Payment received — INV-2025-0042 settled.","waive_outstanding_balance":false} # ReactivateTenantRequest | 

    try:
        # Reactivate a suspended tenant
        api_response = await api_instance.reactivate_tenant(tenant_id, reactivate_tenant_request)
        print("The response of TenantLifecycleApi->reactivate_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->reactivate_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **reactivate_tenant_request** | [**ReactivateTenantRequest**](ReactivateTenantRequest.md)|  | 

### Return type

[**ReactivateTenantResponse**](ReactivateTenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant reactivated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_tenant**
> SuspendTenantResponse suspend_tenant(tenant_id, suspend_tenant_request)

Suspend a tenant

Suspends a tenant for the specified reason. Suspension types include
payment holds (reduced access) and full suspension (no access).
A grace period allows the tenant to resolve the issue before
deletion eligibility. Per NIST SP 800-207 zero-trust principles,
suspended tenants have all active sessions revoked.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.suspend_tenant_request import SuspendTenantRequest
from aqueduct_sdk.models.suspend_tenant_response import SuspendTenantResponse
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
    api_instance = aqueduct_sdk.TenantLifecycleApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    suspend_tenant_request = {"reason":"payment_failed","details":"Invoice INV-2025-0042 overdue by 30 days.","suspension_type":"payment_hold","grace_period_days":14} # SuspendTenantRequest | 

    try:
        # Suspend a tenant
        api_response = await api_instance.suspend_tenant(tenant_id, suspend_tenant_request)
        print("The response of TenantLifecycleApi->suspend_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantLifecycleApi->suspend_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **suspend_tenant_request** | [**SuspendTenantRequest**](SuspendTenantRequest.md)|  | 

### Return type

[**SuspendTenantResponse**](SuspendTenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant suspended. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

