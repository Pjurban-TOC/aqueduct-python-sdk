# aqueduct_sdk.RAGApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](RAGApi.md#add_document) | **POST** /v1/knowledge-bases/{kb_id}/documents | Add a document
[**create_knowledge_base**](RAGApi.md#create_knowledge_base) | **POST** /v1/knowledge-bases | Create a knowledge base
[**delete_document**](RAGApi.md#delete_document) | **DELETE** /v1/knowledge-bases/{kb_id}/documents/{document_id} | Delete a document
[**delete_knowledge_base**](RAGApi.md#delete_knowledge_base) | **DELETE** /v1/knowledge-bases/{kb_id} | Delete a knowledge base
[**get_document**](RAGApi.md#get_document) | **GET** /v1/knowledge-bases/{kb_id}/documents/{document_id} | Get document details
[**get_knowledge_base**](RAGApi.md#get_knowledge_base) | **GET** /v1/knowledge-bases/{kb_id} | Get knowledge base
[**list_documents**](RAGApi.md#list_documents) | **GET** /v1/knowledge-bases/{kb_id}/documents | List documents in a knowledge base
[**list_knowledge_bases**](RAGApi.md#list_knowledge_bases) | **GET** /v1/knowledge-bases | List knowledge bases
[**retrieve_from_knowledge_base**](RAGApi.md#retrieve_from_knowledge_base) | **POST** /v1/rag/retrieve | Retrieve from knowledge base
[**update_knowledge_base**](RAGApi.md#update_knowledge_base) | **PATCH** /v1/knowledge-bases/{kb_id} | Update a knowledge base


# **add_document**
> Document add_document(kb_id, create_document_request)

Add a document

Adds a document to a knowledge base for indexing.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_document_request import CreateDocumentRequest
from aqueduct_sdk.models.document import Document
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 
    create_document_request = {"name":"api-reference-v2.pdf","source":{"type":"s3","uri":"s3://aqueduct-docs/api-reference-v2.pdf"},"metadata":{"category":"api","version":"2.0","department":"engineering"}} # CreateDocumentRequest | 

    try:
        # Add a document
        api_response = await api_instance.add_document(kb_id, create_document_request)
        print("The response of RAGApi->add_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->add_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **create_document_request** | [**CreateDocumentRequest**](CreateDocumentRequest.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document added and queued for indexing. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_knowledge_base**
> KnowledgeBase create_knowledge_base(create_knowledge_base_request)

Create a knowledge base

Creates a new knowledge base for RAG retrieval with configurable chunking and embedding.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.create_knowledge_base_request import CreateKnowledgeBaseRequest
from aqueduct_sdk.models.knowledge_base import KnowledgeBase
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    create_knowledge_base_request = {"name":"Product Documentation","description":"Internal product docs and API references","embedding_model":"text-embedding-3-small","chunking_config":{"strategy":"semantic","max_chunk_size":512,"chunk_overlap":50},"vector_store_config":{"provider":"pgvector"},"privacy_config":{"dp_enabled":false,"access_control":"document_level"}} # CreateKnowledgeBaseRequest | 

    try:
        # Create a knowledge base
        api_response = await api_instance.create_knowledge_base(create_knowledge_base_request)
        print("The response of RAGApi->create_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->create_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_knowledge_base_request** | [**CreateKnowledgeBaseRequest**](CreateKnowledgeBaseRequest.md)|  | 

### Return type

[**KnowledgeBase**](KnowledgeBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Knowledge base created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(kb_id, document_id)

Delete a document

Removes a document and its indexed chunks from a knowledge base.

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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 
    document_id = 'document_id_example' # str | 

    try:
        # Delete a document
        await api_instance.delete_document(kb_id, document_id)
    except Exception as e:
        print("Exception when calling RAGApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **document_id** | **str**|  | 

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
**204** | Document deleted. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_knowledge_base**
> delete_knowledge_base(kb_id)

Delete a knowledge base

Permanently removes a knowledge base and all its documents.

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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 

    try:
        # Delete a knowledge base
        await api_instance.delete_knowledge_base(kb_id)
    except Exception as e:
        print("Exception when calling RAGApi->delete_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 

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
**204** | Knowledge base deleted. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(kb_id, document_id)

Get document details

Returns details and indexing status for a specific document.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.document import Document
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 
    document_id = 'document_id_example' # str | 

    try:
        # Get document details
        api_response = await api_instance.get_document(kb_id, document_id)
        print("The response of RAGApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledge_base**
> KnowledgeBase get_knowledge_base(kb_id)

Get knowledge base

Returns details for a specific knowledge base.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.knowledge_base import KnowledgeBase
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 

    try:
        # Get knowledge base
        api_response = await api_instance.get_knowledge_base(kb_id)
        print("The response of RAGApi->get_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->get_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 

### Return type

[**KnowledgeBase**](KnowledgeBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge base details. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents**
> ListDocuments200Response list_documents(kb_id, page_size=page_size, cursor=cursor, status=status)

List documents in a knowledge base

Returns all documents in a knowledge base with their indexing status.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_documents200_response import ListDocuments200Response
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)
    status = 'status_example' # str |  (optional)

    try:
        # List documents in a knowledge base
        api_response = await api_instance.list_documents(kb_id, page_size=page_size, cursor=cursor, status=status)
        print("The response of RAGApi->list_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->list_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**ListDocuments200Response**](ListDocuments200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_knowledge_bases**
> ListKnowledgeBases200Response list_knowledge_bases(page_size=page_size, cursor=cursor)

List knowledge bases

Returns all knowledge bases for the authenticated tenant.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.list_knowledge_bases200_response import ListKnowledgeBases200Response
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    page_size = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque cursor for pagination. Obtained from `next_cursor` in the previous response. (optional)

    try:
        # List knowledge bases
        api_response = await api_instance.list_knowledge_bases(page_size=page_size, cursor=cursor)
        print("The response of RAGApi->list_knowledge_bases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->list_knowledge_bases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque cursor for pagination. Obtained from &#x60;next_cursor&#x60; in the previous response. | [optional] 

### Return type

[**ListKnowledgeBases200Response**](ListKnowledgeBases200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge base list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_from_knowledge_base**
> RetrievalResponse retrieve_from_knowledge_base(retrieval_request)

Retrieve from knowledge base

Queries a knowledge base and returns relevant document chunks.
Supports hybrid dense/sparse retrieval per DAT [arXiv:2503.23013],
configurable re-ranking per TREC 2025 [arXiv:2603.09891], and
trust/confidence scores per Engineering RAG Stack [arXiv:2601.05264].


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.retrieval_request import RetrievalRequest
from aqueduct_sdk.models.retrieval_response import RetrievalResponse
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    retrieval_request = {"knowledge_base_id":"kb_01HQ3XYZABC123","query":"How do I configure rate limiting?","top_k":5,"score_threshold":0.5,"search_type":"hybrid"} # RetrievalRequest | 

    try:
        # Retrieve from knowledge base
        api_response = await api_instance.retrieve_from_knowledge_base(retrieval_request)
        print("The response of RAGApi->retrieve_from_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->retrieve_from_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieval_request** | [**RetrievalRequest**](RetrievalRequest.md)|  | 

### Return type

[**RetrievalResponse**](RetrievalResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieval results. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledge_base**
> KnowledgeBase update_knowledge_base(kb_id, update_knowledge_base_request)

Update a knowledge base

Updates knowledge base configuration.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.knowledge_base import KnowledgeBase
from aqueduct_sdk.models.update_knowledge_base_request import UpdateKnowledgeBaseRequest
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
    api_instance = aqueduct_sdk.RAGApi(api_client)
    kb_id = 'kb_id_example' # str | 
    update_knowledge_base_request = {"name":"Product Documentation v2","description":"Updated internal product docs with new API v2 references","chunking_config":{"strategy":"contextual","max_chunk_size":1024,"chunk_overlap":100}} # UpdateKnowledgeBaseRequest | 

    try:
        # Update a knowledge base
        api_response = await api_instance.update_knowledge_base(kb_id, update_knowledge_base_request)
        print("The response of RAGApi->update_knowledge_base:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RAGApi->update_knowledge_base: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kb_id** | **str**|  | 
 **update_knowledge_base_request** | [**UpdateKnowledgeBaseRequest**](UpdateKnowledgeBaseRequest.md)|  | 

### Return type

[**KnowledgeBase**](KnowledgeBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Knowledge base updated. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

