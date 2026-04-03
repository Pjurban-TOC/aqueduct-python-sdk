# aqueduct_sdk.InferenceApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chat_completion**](InferenceApi.md#create_chat_completion) | **POST** /v1/chat/completions | Create chat completion
[**create_embedding**](InferenceApi.md#create_embedding) | **POST** /v1/embeddings | Create embeddings
[**list_models**](InferenceApi.md#list_models) | **GET** /v1/models | List available models


# **create_chat_completion**
> ChatCompletionResponse create_chat_completion(chat_completion_request, x_model_override=x_model_override, x_route_config=x_route_config, x_provider_override=x_provider_override, x_cache_control=x_cache_control)

Create chat completion

OpenAI-compatible chat completion endpoint. Supports both synchronous
(JSON) and streaming (SSE) responses based on the `stream` parameter.

This is the primary AI inference endpoint. Requests are routed to the
appropriate upstream provider based on tenant configuration, model
availability, and routing policy.

**Streaming:** When `stream: true`, the response uses `text/event-stream`
content type with `ChatCompletionChunk` objects. The stream terminates
with `data: [DONE]`.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.chat_completion_request import ChatCompletionRequest
from aqueduct_sdk.models.chat_completion_response import ChatCompletionResponse
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.InferenceApi(api_client)
    chat_completion_request = {"model":"gpt-4o","messages":[{"role":"system","content":"You are a helpful assistant."},{"role":"user","content":"Explain quantum computing in simple terms."}],"temperature":0.7,"max_tokens":1024} # ChatCompletionRequest | 
    x_model_override = 'gpt-4o' # str | Override the model selection for this request, bypassing the routing policy. Requires `model:invoke` scope and the model must be in the tenant's `models_allowed` list. (optional)
    x_route_config = 'x_route_config_example' # str | Named routing configuration to apply (e.g., `low-latency`, `cost-optimized`). Configured per-tenant. (optional)
    x_provider_override = 'x_provider_override_example' # str | Force routing to a specific provider backend (e.g., `openai`, `anthropic`, `azure`). Follows the Portkey routing header pattern. (optional)
    x_cache_control = 'x_cache_control_example' # str | Controls response cache behavior for this request. - `no-cache`: Skip cache read (force fresh LLM call), but still store the   new response in cache for subsequent requests. - `no-store`: Skip cache read AND write. The response is neither served from   cache nor stored. Use for sensitive queries that should never be cached. Omitting this header (default) enables normal cache behavior. Per Key Collision Attack [arXiv:2601.23088], caches are strictly tenant-isolated to prevent cross-tenant poisoning.  (optional)

    try:
        # Create chat completion
        api_response = await api_instance.create_chat_completion(chat_completion_request, x_model_override=x_model_override, x_route_config=x_route_config, x_provider_override=x_provider_override, x_cache_control=x_cache_control)
        print("The response of InferenceApi->create_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_chat_completion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_completion_request** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 
 **x_model_override** | **str**| Override the model selection for this request, bypassing the routing policy. Requires &#x60;model:invoke&#x60; scope and the model must be in the tenant&#39;s &#x60;models_allowed&#x60; list. | [optional] 
 **x_route_config** | **str**| Named routing configuration to apply (e.g., &#x60;low-latency&#x60;, &#x60;cost-optimized&#x60;). Configured per-tenant. | [optional] 
 **x_provider_override** | **str**| Force routing to a specific provider backend (e.g., &#x60;openai&#x60;, &#x60;anthropic&#x60;, &#x60;azure&#x60;). Follows the Portkey routing header pattern. | [optional] 
 **x_cache_control** | **str**| Controls response cache behavior for this request. - &#x60;no-cache&#x60;: Skip cache read (force fresh LLM call), but still store the   new response in cache for subsequent requests. - &#x60;no-store&#x60;: Skip cache read AND write. The response is neither served from   cache nor stored. Use for sensitive queries that should never be cached. Omitting this header (default) enables normal cache behavior. Per Key Collision Attack [arXiv:2601.23088], caches are strictly tenant-isolated to prevent cross-tenant poisoning.  | [optional] 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat completion response. Content type depends on the &#x60;stream&#x60; parameter: - &#x60;stream: false&#x60; (default): &#x60;application/json&#x60; with &#x60;ChatCompletionResponse&#x60; - &#x60;stream: true&#x60;: &#x60;text/event-stream&#x60; with &#x60;ChatCompletionChunk&#x60; objects  |  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  * X-Tenant-ID -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  * X-RateLimit-Reset-Tokens -  <br>  * X-RateLimit-Reset-Requests -  <br>  * X-Cache-Status -  <br>  * X-Cache-Age -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**413** | Request body exceeds maximum size (ERR-API-001-013). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**500** | Unexpected server error (ERR-API-001-012). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**502** | Upstream LLM provider returned an error (ERR-API-001-009). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**503** | Service unavailable due to circuit breaker open (ERR-API-001-011). Includes &#x60;Retry-After&#x60; header.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  |
**504** | Upstream service timed out (ERR-API-001-010). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedding**
> EmbeddingResponse create_embedding(embedding_request)

Create embeddings

OpenAI-compatible embedding endpoint. Generates vector representations
of input text for similarity search, clustering, and RAG retrieval.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.embedding_request import EmbeddingRequest
from aqueduct_sdk.models.embedding_response import EmbeddingResponse
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.InferenceApi(api_client)
    embedding_request = {"model":"text-embedding-3-small","input":"The food was delicious and the waiter was friendly."} # EmbeddingRequest | 

    try:
        # Create embeddings
        api_response = await api_instance.create_embedding(embedding_request)
        print("The response of InferenceApi->create_embedding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->create_embedding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embedding_request** | [**EmbeddingRequest**](EmbeddingRequest.md)|  | 

### Return type

[**EmbeddingResponse**](EmbeddingResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Embedding response. |  * X-Trace-ID -  <br>  * RateLimit -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**429** | Rate limit exceeded (ERR-API-001-001). Includes &#x60;Retry-After&#x60; header and IETF-standard rate limit headers.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * Retry-After -  <br>  * RateLimit -  <br>  * RateLimit-Policy -  <br>  * X-RateLimit-Remaining-Tokens -  <br>  * X-RateLimit-Remaining-Requests -  <br>  |
**502** | Upstream LLM provider returned an error (ERR-API-001-009). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_models**
> ListModelsResponse list_models()

List available models

Returns models available to the authenticated tenant based on their
plan tier and allowed models configuration.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_models_response import ListModelsResponse
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = aqueduct_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with aqueduct_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aqueduct_sdk.InferenceApi(api_client)

    try:
        # List available models
        api_response = await api_instance.list_models()
        print("The response of InferenceApi->list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InferenceApi->list_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListModelsResponse**](ListModelsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

