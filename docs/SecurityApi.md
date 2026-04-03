# aqueduct_sdk.SecurityApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate_hsm_key**](SecurityApi.md#deactivate_hsm_key) | **POST** /api/v1/hsm/keys/{keyID}/deactivate | Deactivate an HSM key
[**destroy_hsm_key**](SecurityApi.md#destroy_hsm_key) | **DELETE** /api/v1/hsm/keys/{keyID} | Destroy an HSM key
[**generate_hsm_key**](SecurityApi.md#generate_hsm_key) | **POST** /api/v1/hsm/keys | Generate a new HSM key
[**get_hsm_health**](SecurityApi.md#get_hsm_health) | **GET** /api/v1/hsm/health | Get HSM health and FIPS self-test status
[**get_hsm_key_attestation**](SecurityApi.md#get_hsm_key_attestation) | **GET** /api/v1/hsm/keys/{keyID}/attestation | Get key attestation evidence
[**get_hsm_key_metadata**](SecurityApi.md#get_hsm_key_metadata) | **GET** /api/v1/hsm/keys/{keyID} | Get HSM key metadata
[**hsm_decrypt**](SecurityApi.md#hsm_decrypt) | **POST** /api/v1/hsm/decrypt | Decrypt data
[**hsm_encrypt**](SecurityApi.md#hsm_encrypt) | **POST** /api/v1/hsm/encrypt | Encrypt data
[**hsm_sign**](SecurityApi.md#hsm_sign) | **POST** /api/v1/hsm/sign | Sign data
[**hsm_unwrap_key**](SecurityApi.md#hsm_unwrap_key) | **POST** /api/v1/hsm/unwrap | Unwrap a key
[**hsm_verify**](SecurityApi.md#hsm_verify) | **POST** /api/v1/hsm/verify | Verify a signature
[**hsm_wrap_key**](SecurityApi.md#hsm_wrap_key) | **POST** /api/v1/hsm/wrap | Wrap a key
[**list_hsm_keys**](SecurityApi.md#list_hsm_keys) | **GET** /api/v1/hsm/keys | List HSM keys
[**rotate_hsm_key**](SecurityApi.md#rotate_hsm_key) | **POST** /api/v1/hsm/keys/{keyID}/rotate | Rotate an HSM key


# **deactivate_hsm_key**
> DeactivateKeyResponse deactivate_hsm_key(key_id)

Deactivate an HSM key

Transitions a key from active to deactivated state per NIST SP 800-57.
Deactivated keys can still be used for decryption but not encryption.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.deactivate_key_response import DeactivateKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    key_id = 'key_01HQ3XYZABC123' # str | HSM key identifier.

    try:
        # Deactivate an HSM key
        api_response = await api_instance.deactivate_hsm_key(key_id)
        print("The response of SecurityApi->deactivate_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->deactivate_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| HSM key identifier. | 

### Return type

[**DeactivateKeyResponse**](DeactivateKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key deactivated. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_hsm_key**
> DestroyKeyResponse destroy_hsm_key(key_id)

Destroy an HSM key

Permanently destroys an HSM key with FIPS 140-3 zeroization.
Key must be in deactivated state. This action is irreversible.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.destroy_key_response import DestroyKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    key_id = 'key_01HQ3XYZABC123' # str | HSM key identifier.

    try:
        # Destroy an HSM key
        api_response = await api_instance.destroy_hsm_key(key_id)
        print("The response of SecurityApi->destroy_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->destroy_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| HSM key identifier. | 

### Return type

[**DestroyKeyResponse**](DestroyKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key destroyed. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**409** | Resource conflict (ERR-API-001-014). The request could not be completed due to a conflict with the current state of the target resource.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_hsm_key**
> GenerateKeyResponse generate_hsm_key(generate_key_request)

Generate a new HSM key

Generates a new cryptographic key in the HSM. Supports classical
(AES-256, RSA, ECDSA, Ed25519) and post-quantum (ML-KEM, ML-DSA,
SLH-DSA) key types per NIST IR 8547 PQC readiness timeline.
New keys start in pre-operational state per NIST SP 800-57.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.generate_key_request import GenerateKeyRequest
from aqueduct_sdk.models.generate_key_response import GenerateKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    generate_key_request = {"key_type":"AES-256","label":"tenant-dek-acme-corp"} # GenerateKeyRequest | 

    try:
        # Generate a new HSM key
        api_response = await api_instance.generate_hsm_key(generate_key_request)
        print("The response of SecurityApi->generate_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->generate_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_key_request** | [**GenerateKeyRequest**](GenerateKeyRequest.md)|  | 

### Return type

[**GenerateKeyResponse**](GenerateKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Key generated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hsm_health**
> HSMHealthResponse get_hsm_health()

Get HSM health and FIPS self-test status

Returns HSM connectivity, FIPS 140-3 self-test results, session
availability, and active key count. Used for operational monitoring.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.hsm_health_response import HSMHealthResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)

    try:
        # Get HSM health and FIPS self-test status
        api_response = await api_instance.get_hsm_health()
        print("The response of SecurityApi->get_hsm_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_hsm_health: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HSMHealthResponse**](HSMHealthResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HSM health status. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**503** | Service unavailable due to circuit breaker open (ERR-API-001-011). Includes &#x60;Retry-After&#x60; header.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hsm_key_attestation**
> AttestationResponse get_hsm_key_attestation(key_id)

Get key attestation evidence

Returns cryptographic attestation evidence proving the key was generated
and is stored within a FIPS 140-3 validated HSM. Follows IETF RATS
(RFC 9334) remote attestation pattern.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.attestation_response import AttestationResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    key_id = 'key_01HQ3XYZABC123' # str | HSM key identifier.

    try:
        # Get key attestation evidence
        api_response = await api_instance.get_hsm_key_attestation(key_id)
        print("The response of SecurityApi->get_hsm_key_attestation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_hsm_key_attestation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| HSM key identifier. | 

### Return type

[**AttestationResponse**](AttestationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attestation evidence. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hsm_key_metadata**
> HSMKeyMetadata get_hsm_key_metadata(key_id)

Get HSM key metadata

Returns metadata for a specific HSM key. Does not expose key material.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.hsm_key_metadata import HSMKeyMetadata
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    key_id = 'key_01HQ3XYZABC123' # str | HSM key identifier.

    try:
        # Get HSM key metadata
        api_response = await api_instance.get_hsm_key_metadata(key_id)
        print("The response of SecurityApi->get_hsm_key_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_hsm_key_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| HSM key identifier. | 

### Return type

[**HSMKeyMetadata**](HSMKeyMetadata.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key metadata. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_decrypt**
> DecryptResponse hsm_decrypt(decrypt_request)

Decrypt data

Decrypts data previously encrypted with `hsmEncrypt`.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.decrypt_request import DecryptRequest
from aqueduct_sdk.models.decrypt_response import DecryptResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    decrypt_request = {"key_id":"key_01HQ3XYZABC123","ciphertext":"kJ3nF8gH2mPq...base64...","nonce":"dW5pcXVlX25vbmNl","aad":"dGVuYW50X2FjbWU="} # DecryptRequest | 

    try:
        # Decrypt data
        api_response = await api_instance.hsm_decrypt(decrypt_request)
        print("The response of SecurityApi->hsm_decrypt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_decrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decrypt_request** | [**DecryptRequest**](DecryptRequest.md)|  | 

### Return type

[**DecryptResponse**](DecryptResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Decrypted data. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_encrypt**
> EncryptResponse hsm_encrypt(encrypt_request)

Encrypt data

Encrypts data using AES-256-GCM with a 96-bit nonce per
NIST SP 800-38D. Supports additional authenticated data (AAD)
for authenticated encryption.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.encrypt_request import EncryptRequest
from aqueduct_sdk.models.encrypt_response import EncryptResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    encrypt_request = {"key_id":"key_01HQ3XYZABC123","plaintext":"SGVsbG8gV29ybGQ=","aad":"dGVuYW50X2FjbWU="} # EncryptRequest | 

    try:
        # Encrypt data
        api_response = await api_instance.hsm_encrypt(encrypt_request)
        print("The response of SecurityApi->hsm_encrypt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_encrypt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encrypt_request** | [**EncryptRequest**](EncryptRequest.md)|  | 

### Return type

[**EncryptResponse**](EncryptResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encrypted data. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_sign**
> SignResponse hsm_sign(sign_request)

Sign data

Creates a digital signature over a digest using an asymmetric key
(RSA, ECDSA, Ed25519, ML-DSA). The caller provides a pre-computed
digest (SHA-256 or SHA-384).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.sign_request import SignRequest
from aqueduct_sdk.models.sign_response import SignResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    sign_request = {"key_id":"key_01HQ3ECDSA_P256","digest":"n4bQgYhMfWWaL+qgxVrQFaO/TxsrC4Is0V1sFbDwCgg="} # SignRequest | 

    try:
        # Sign data
        api_response = await api_instance.hsm_sign(sign_request)
        print("The response of SecurityApi->hsm_sign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_sign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_request** | [**SignRequest**](SignRequest.md)|  | 

### Return type

[**SignResponse**](SignResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signature. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_unwrap_key**
> UnwrapKeyResponse hsm_unwrap_key(unwrap_key_request)

Unwrap a key

Unwraps (decrypts) a wrapped DEK using the specified KEK via
AES-KWP per RFC 5649 / NIST SP 800-38F.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.unwrap_key_request import UnwrapKeyRequest
from aqueduct_sdk.models.unwrap_key_response import UnwrapKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    unwrap_key_request = {"kek_id":"key_01HQ3KEK_MASTER","wrapped_dek":"oL2nPq7Rs8Tu...wrapped-base64..."} # UnwrapKeyRequest | 

    try:
        # Unwrap a key
        api_response = await api_instance.hsm_unwrap_key(unwrap_key_request)
        print("The response of SecurityApi->hsm_unwrap_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_unwrap_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unwrap_key_request** | [**UnwrapKeyRequest**](UnwrapKeyRequest.md)|  | 

### Return type

[**UnwrapKeyResponse**](UnwrapKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unwrapped key. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_verify**
> VerifyResponse hsm_verify(verify_request)

Verify a signature

Verifies a digital signature against a digest using the corresponding public key.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.verify_request import VerifyRequest
from aqueduct_sdk.models.verify_response import VerifyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    verify_request = {"key_id":"key_01HQ3ECDSA_P256","digest":"n4bQgYhMfWWaL+qgxVrQFaO/TxsrC4Is0V1sFbDwCgg=","signature":"MEUCIQDx...base64-signature..."} # VerifyRequest | 

    try:
        # Verify a signature
        api_response = await api_instance.hsm_verify(verify_request)
        print("The response of SecurityApi->hsm_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_request** | [**VerifyRequest**](VerifyRequest.md)|  | 

### Return type

[**VerifyResponse**](VerifyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verification result. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hsm_wrap_key**
> WrapKeyResponse hsm_wrap_key(wrap_key_request)

Wrap a key

Wraps (encrypts) a data encryption key (DEK) using a key encryption
key (KEK) via AES-KWP per RFC 5649 / NIST SP 800-38F. Used for
secure key transport in the envelope encryption hierarchy.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.wrap_key_request import WrapKeyRequest
from aqueduct_sdk.models.wrap_key_response import WrapKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    wrap_key_request = {"kek_id":"key_01HQ3KEK_MASTER","dek":"AQIDBAUGBwgJCgsMDQ4PEA=="} # WrapKeyRequest | 

    try:
        # Wrap a key
        api_response = await api_instance.hsm_wrap_key(wrap_key_request)
        print("The response of SecurityApi->hsm_wrap_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->hsm_wrap_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wrap_key_request** | [**WrapKeyRequest**](WrapKeyRequest.md)|  | 

### Return type

[**WrapKeyResponse**](WrapKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Wrapped key. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hsm_keys**
> ListKeysResponse list_hsm_keys(state=state, key_type=key_type, label=label, limit=limit)

List HSM keys

Returns HSM key metadata filtered by state, type, or label.
Does not expose key material — only metadata per NIST SP 800-57.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.hsm_key_state import HSMKeyState
from aqueduct_sdk.models.hsm_key_type import HSMKeyType
from aqueduct_sdk.models.list_keys_response import ListKeysResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    state = aqueduct_sdk.HSMKeyState() # HSMKeyState | Filter by key state (NIST SP 800-57 lifecycle). (optional)
    key_type = aqueduct_sdk.HSMKeyType() # HSMKeyType | Filter by key type. (optional)
    label = 'label_example' # str | Filter by label prefix. (optional)
    limit = 20 # int | Maximum keys to return. (optional) (default to 20)

    try:
        # List HSM keys
        api_response = await api_instance.list_hsm_keys(state=state, key_type=key_type, label=label, limit=limit)
        print("The response of SecurityApi->list_hsm_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->list_hsm_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**HSMKeyState**](.md)| Filter by key state (NIST SP 800-57 lifecycle). | [optional] 
 **key_type** | [**HSMKeyType**](.md)| Filter by key type. | [optional] 
 **label** | **str**| Filter by label prefix. | [optional] 
 **limit** | **int**| Maximum keys to return. | [optional] [default to 20]

### Return type

[**ListKeysResponse**](ListKeysResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key metadata list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_hsm_key**
> RotateKeyResponse rotate_hsm_key(key_id)

Rotate an HSM key

Creates a new version of the key. The previous version is deactivated
per NIST SP 800-57 crypto-period management. Existing ciphertext
encrypted with the old version remains decryptable.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.rotate_key_response import RotateKeyResponse
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
    api_instance = aqueduct_sdk.SecurityApi(api_client)
    key_id = 'key_01HQ3XYZABC123' # str | HSM key identifier.

    try:
        # Rotate an HSM key
        api_response = await api_instance.rotate_hsm_key(key_id)
        print("The response of SecurityApi->rotate_hsm_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->rotate_hsm_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| HSM key identifier. | 

### Return type

[**RotateKeyResponse**](RotateKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key rotated. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

