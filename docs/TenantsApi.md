# aqueduct_sdk.TenantsApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](TenantsApi.md#add_domain) | **POST** /api/v1/tenants/{tenant_id}/domains | Add a custom domain
[**create_tenant**](TenantsApi.md#create_tenant) | **POST** /api/v1/tenants | Create a new tenant
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /api/v1/tenants/{tenant_id} | Delete a tenant
[**get_domain**](TenantsApi.md#get_domain) | **GET** /api/v1/tenants/{tenant_id}/domains/{domain_id} | Get domain details
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /api/v1/tenants/{tenant_id} | Get tenant by ID
[**list_domains**](TenantsApi.md#list_domains) | **GET** /api/v1/tenants/{tenant_id}/domains | List tenant domains
[**list_tenants**](TenantsApi.md#list_tenants) | **GET** /api/v1/tenants | List tenants
[**remove_domain**](TenantsApi.md#remove_domain) | **DELETE** /api/v1/tenants/{tenant_id}/domains/{domain_id} | Remove a custom domain
[**update_tenant_config**](TenantsApi.md#update_tenant_config) | **PATCH** /api/v1/tenants/{tenant_id}/config | Update tenant configuration
[**update_tenant_status**](TenantsApi.md#update_tenant_status) | **POST** /api/v1/tenants/{tenant_id}/status | Update tenant status
[**verify_domain**](TenantsApi.md#verify_domain) | **POST** /api/v1/tenants/{tenant_id}/domains/{domain_id}/verify | Trigger domain verification


# **add_domain**
> AddDomainResponse add_domain(tenant_id, add_domain_request)

Add a custom domain

Registers a custom domain for a tenant. Returns DNS verification
instructions that must be completed before the domain is active.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.add_domain_request import AddDomainRequest
from aqueduct_sdk.models.add_domain_response import AddDomainResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    add_domain_request = {"domain":"api.acme.example.com","type":"api"} # AddDomainRequest | 

    try:
        # Add a custom domain
        api_response = await api_instance.add_domain(tenant_id, add_domain_request)
        print("The response of TenantsApi->add_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->add_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **add_domain_request** | [**AddDomainRequest**](AddDomainRequest.md)|  | 

### Return type

[**AddDomainResponse**](AddDomainResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain registered. Complete DNS verification to activate. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant**
> TenantResponse create_tenant(create_tenant_request)

Create a new tenant

Provisions a new tenant with the specified configuration. The tenant ID is
generated from the slug with a random suffix: `tnt_{slug}_{suffix}`.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_tenant_request import CreateTenantRequest
from aqueduct_sdk.models.tenant_response import TenantResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    create_tenant_request = {"name":"Acme Corp","slug":"acme-corp","tier":"enterprise","region":"us-east-1","admin_email":"admin@acme.example.com","config":{"session_timeout_minutes":30,"mfa_required":true,"ip_allowlist":["10.0.0.0/8"]}} # CreateTenantRequest | 

    try:
        # Create a new tenant
        api_response = await api_instance.create_tenant(create_tenant_request)
        print("The response of TenantsApi->create_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tenant_request** | [**CreateTenantRequest**](CreateTenantRequest.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tenant created successfully. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> DeleteTenantResponse delete_tenant(tenant_id, delete_tenant_request)

Delete a tenant

Schedules a tenant for deletion with a 72-hour grace period.
Requires confirmation by providing the tenant slug. Data export
can be requested before deletion.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.delete_tenant_request import DeleteTenantRequest
from aqueduct_sdk.models.delete_tenant_response import DeleteTenantResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    delete_tenant_request = {"confirmation":"acme-corp","reason":"Organization dissolved per legal request","export_data":true} # DeleteTenantRequest | 

    try:
        # Delete a tenant
        api_response = await api_instance.delete_tenant(tenant_id, delete_tenant_request)
        print("The response of TenantsApi->delete_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **delete_tenant_request** | [**DeleteTenantRequest**](DeleteTenantRequest.md)|  | 

### Return type

[**DeleteTenantResponse**](DeleteTenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant scheduled for deletion. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainResponse get_domain(tenant_id, domain_id)

Get domain details

Returns detailed information about a specific domain including verification and SSL status.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.domain_response import DomainResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    domain_id = 'domain_id_example' # str | Domain identifier.

    try:
        # Get domain details
        api_response = await api_instance.get_domain(tenant_id, domain_id)
        print("The response of TenantsApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **domain_id** | **str**| Domain identifier. | 

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> TenantResponse get_tenant(tenant_id)

Get tenant by ID

Returns detailed information about a specific tenant. Users can access
their own tenant; system admins can access any tenant.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.tenant_response import TenantResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # Get tenant by ID
        api_response = await api_instance.get_tenant(tenant_id)
        print("The response of TenantsApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> DomainListResponse list_domains(tenant_id)

List tenant domains

Returns all custom domains registered for a tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.domain_list_response import DomainListResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.

    try:
        # List tenant domains
        api_response = await api_instance.list_domains(tenant_id)
        print("The response of TenantsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->list_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 

### Return type

[**DomainListResponse**](DomainListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tenants**
> ListTenantsResponse list_tenants(page_size=page_size, cursor=cursor, tier=tier, status=status, region=region)

List tenants

Returns a paginated list of tenants. System admins see all tenants;
reseller admins see tenants within their organization.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_tenants_response import ListTenantsResponse
from aqueduct_sdk.models.tenant_status import TenantStatus
from aqueduct_sdk.models.tenant_tier import TenantTier
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)
    tier = aqueduct_sdk.TenantTier() # TenantTier |  (optional)
    status = aqueduct_sdk.TenantStatus() # TenantStatus |  (optional)
    region = 'region_example' # str |  (optional)

    try:
        # List tenants
        api_response = await api_instance.list_tenants(page_size=page_size, cursor=cursor, tier=tier, status=status, region=region)
        print("The response of TenantsApi->list_tenants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->list_tenants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 
 **tier** | [**TenantTier**](.md)|  | [optional] 
 **status** | [**TenantStatus**](.md)|  | [optional] 
 **region** | **str**|  | [optional] 

### Return type

[**ListTenantsResponse**](ListTenantsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated tenant list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain**
> RemoveDomainResponse remove_domain(tenant_id, domain_id)

Remove a custom domain

Removes a custom domain from a tenant. A grace period applies before
full removal to prevent accidental disruption.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.remove_domain_response import RemoveDomainResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    domain_id = 'domain_id_example' # str | Domain identifier.

    try:
        # Remove a custom domain
        api_response = await api_instance.remove_domain(tenant_id, domain_id)
        print("The response of TenantsApi->remove_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->remove_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **domain_id** | **str**| Domain identifier. | 

### Return type

[**RemoveDomainResponse**](RemoveDomainResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain scheduled for removal. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_config**
> TenantResponse update_tenant_config(tenant_id, update_config_request)

Update tenant configuration

Updates the configuration for a specific tenant. Only provided fields
are updated (partial update).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.tenant_response import TenantResponse
from aqueduct_sdk.models.update_config_request import UpdateConfigRequest
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    update_config_request = {"session_timeout_minutes":60,"mfa_required":true,"ip_allowlist":["10.0.0.0/8","172.16.0.0/12"]} # UpdateConfigRequest | 

    try:
        # Update tenant configuration
        api_response = await api_instance.update_tenant_config(tenant_id, update_config_request)
        print("The response of TenantsApi->update_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **update_config_request** | [**UpdateConfigRequest**](UpdateConfigRequest.md)|  | 

### Return type

[**TenantResponse**](TenantResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_status**
> StatusUpdateResponse update_tenant_status(tenant_id, status_update_request)

Update tenant status

Changes a tenant's lifecycle status (e.g., active -> suspended).
Status transitions are validated server-side.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.status_update_request import StatusUpdateRequest
from aqueduct_sdk.models.status_update_response import StatusUpdateResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    status_update_request = {"status":"suspended","reason":"Suspended due to billing non-payment"} # StatusUpdateRequest | 

    try:
        # Update tenant status
        api_response = await api_instance.update_tenant_status(tenant_id, status_update_request)
        print("The response of TenantsApi->update_tenant_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->update_tenant_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **status_update_request** | [**StatusUpdateRequest**](StatusUpdateRequest.md)|  | 

### Return type

[**StatusUpdateResponse**](StatusUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_domain**
> VerifyDomainResponse verify_domain(tenant_id, domain_id)

Trigger domain verification

Manually triggers DNS verification for a domain. The system checks for
the expected DNS TXT record and updates verification status.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.verify_domain_response import VerifyDomainResponse
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
    api_instance = aqueduct_sdk.TenantsApi(api_client)
    tenant_id = 'tnt_acme-corp_a1b2c3' # str | Tenant identifier matching the pattern `tnt_{slug}_{suffix}`.
    domain_id = 'domain_id_example' # str | Domain identifier.

    try:
        # Trigger domain verification
        api_response = await api_instance.verify_domain(tenant_id, domain_id)
        print("The response of TenantsApi->verify_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->verify_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Tenant identifier matching the pattern &#x60;tnt_{slug}_{suffix}&#x60;. | 
 **domain_id** | **str**| Domain identifier. | 

### Return type

[**VerifyDomainResponse**](VerifyDomainResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification result. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

