# aqueduct_sdk.AuthenticationApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session**](AuthenticationApi.md#delete_session) | **DELETE** /api/v1/auth/sessions/{session_id} | Terminate a session
[**get_jwks**](AuthenticationApi.md#get_jwks) | **GET** /.well-known/jwks.json | Get JSON Web Key Set
[**list_sessions**](AuthenticationApi.md#list_sessions) | **GET** /api/v1/auth/sessions | List active sessions
[**refresh_token**](AuthenticationApi.md#refresh_token) | **POST** /api/v1/auth/token/refresh | Refresh an access token
[**revoke_token**](AuthenticationApi.md#revoke_token) | **POST** /api/v1/auth/token/revoke | Revoke a token
[**validate_token**](AuthenticationApi.md#validate_token) | **POST** /api/v1/auth/validate | Validate an access token


# **delete_session**
> DeleteSession200Response delete_session(session_id)

Terminate a session

Terminates a specific session, revoking all associated tokens.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.delete_session200_response import DeleteSession200Response
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)
    session_id = 'session_id_example' # str | Session identifier to terminate.

    try:
        # Terminate a session
        api_response = await api_instance.delete_session(session_id)
        print("The response of AuthenticationApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Session identifier to terminate. | 

### Return type

[**DeleteSession200Response**](DeleteSession200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session terminated. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwks**
> JWKSet get_jwks()

Get JSON Web Key Set

Returns the public keys used to verify JWT tokens issued by the auth service.
Follows the [RFC 7517 (JWK)](https://www.rfc-editor.org/rfc/rfc7517) standard.
Clients should cache this response and refresh periodically.


### Example


```python
import aqueduct_sdk
from aqueduct_sdk.models.jwk_set import JWKSet
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)

    try:
        # Get JSON Web Key Set
        api_response = await api_instance.get_jwks()
        print("The response of AuthenticationApi->get_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_jwks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JWKSet**](JWKSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON Web Key Set. |  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> ListSessionsResponse list_sessions()

List active sessions

Returns all active sessions for the authenticated user.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_sessions_response import ListSessionsResponse
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)

    try:
        # List active sessions
        api_response = await api_instance.list_sessions()
        print("The response of AuthenticationApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->list_sessions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListSessionsResponse**](ListSessionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active sessions. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> RefreshTokenResponse refresh_token(refresh_token_request)

Refresh an access token

Exchange a refresh token for a new access token and rotated refresh token.
The old refresh token is invalidated after use (one-time use).


### Example


```python
import aqueduct_sdk
from aqueduct_sdk.models.refresh_token_request import RefreshTokenRequest
from aqueduct_sdk.models.refresh_token_response import RefreshTokenResponse
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)
    refresh_token_request = {"refresh_token":"dGhpcyBpcyBhIHJlZnJlc2ggdG9rZW4...","session_id":"ses_01HQ3XYZABC123"} # RefreshTokenRequest | 

    try:
        # Refresh an access token
        api_response = await api_instance.refresh_token(refresh_token_request)
        print("The response of AuthenticationApi->refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_request** | [**RefreshTokenRequest**](RefreshTokenRequest.md)|  | 

### Return type

[**RefreshTokenResponse**](RefreshTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New token pair. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> RevokeToken200Response revoke_token(revoke_token_request)

Revoke a token

Revokes an access or refresh token. Supports explicit context
destruction for session lifecycle management.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.revoke_token200_response import RevokeToken200Response
from aqueduct_sdk.models.revoke_token_request import RevokeTokenRequest
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)
    revoke_token_request = {"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFxdWVkdWN0LTIwMjUtMDEifQ.eyJzdWIiOiJ1c3Jfam9obmRvZV9hYmMxMjMifQ.signature","reason":"user_logout"} # RevokeTokenRequest | 

    try:
        # Revoke a token
        api_response = await api_instance.revoke_token(revoke_token_request)
        print("The response of AuthenticationApi->revoke_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->revoke_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_token_request** | [**RevokeTokenRequest**](RevokeTokenRequest.md)|  | 

### Return type

[**RevokeToken200Response**](RevokeToken200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token revoked. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_token**
> ValidateTokenResponse validate_token(validate_token_request)

Validate an access token

Validates a JWT access token and returns decoded claims if valid.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.validate_token_request import ValidateTokenRequest
from aqueduct_sdk.models.validate_token_response import ValidateTokenResponse
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
    api_instance = aqueduct_sdk.AuthenticationApi(api_client)
    validate_token_request = {"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFxdWVkdWN0LTIwMjUtMDEifQ.eyJzdWIiOiJ1c3Jfam9obmRvZV9hYmMxMjMiLCJ0aWQiOiJ0bnRfYWNtZS1jb3JwX2ExYjJjMyJ9.signature"} # ValidateTokenRequest | 

    try:
        # Validate an access token
        api_response = await api_instance.validate_token(validate_token_request)
        print("The response of AuthenticationApi->validate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->validate_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_token_request** | [**ValidateTokenRequest**](ValidateTokenRequest.md)|  | 

### Return type

[**ValidateTokenResponse**](ValidateTokenResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token validation result. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

