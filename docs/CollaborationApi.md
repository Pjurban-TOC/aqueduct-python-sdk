# aqueduct_sdk.CollaborationApi

All URIs are relative to *https://api.aqueduct.io:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_workspace_member**](CollaborationApi.md#add_workspace_member) | **POST** /api/v1/workspaces/{workspace_id}/members | Add a member to a workspace
[**create_annotation**](CollaborationApi.md#create_annotation) | **POST** /api/v1/conversations/{conversation_id}/turns/{turn_index}/annotations | Create an annotation on a conversation turn
[**delete_annotation**](CollaborationApi.md#delete_annotation) | **DELETE** /api/v1/conversations/{conversation_id}/turns/{turn_index}/annotations/{annotation_id} | Delete an annotation
[**list_annotations**](CollaborationApi.md#list_annotations) | **GET** /api/v1/conversations/{conversation_id}/turns/{turn_index}/annotations | List annotations for a conversation turn
[**list_collab_activity**](CollaborationApi.md#list_collab_activity) | **GET** /api/v1/activity | List collaboration activity records
[**list_conversation_shares**](CollaborationApi.md#list_conversation_shares) | **GET** /api/v1/conversations/{conversation_id}/shares | List shares for a conversation
[**list_presence**](CollaborationApi.md#list_presence) | **GET** /api/v1/presence | List active presence records for a conversation
[**list_workspace_members**](CollaborationApi.md#list_workspace_members) | **GET** /api/v1/workspaces/{workspace_id}/members | List workspace members
[**presence_web_socket**](CollaborationApi.md#presence_web_socket) | **GET** /api/v1/presence/ws | Subscribe to real-time presence events via WebSocket
[**remove_workspace_member**](CollaborationApi.md#remove_workspace_member) | **DELETE** /api/v1/workspaces/{workspace_id}/members/{user_id} | Remove a member from a workspace
[**revoke_conversation_share**](CollaborationApi.md#revoke_conversation_share) | **DELETE** /api/v1/conversations/{conversation_id}/shares/{share_id} | Revoke a share
[**share_conversation**](CollaborationApi.md#share_conversation) | **POST** /api/v1/conversations/{conversation_id}/shares | Share a conversation with a user, role, or team
[**update_annotation**](CollaborationApi.md#update_annotation) | **PUT** /api/v1/conversations/{conversation_id}/turns/{turn_index}/annotations/{annotation_id} | Update an annotation body
[**update_workspace_member_role**](CollaborationApi.md#update_workspace_member_role) | **PUT** /api/v1/workspaces/{workspace_id}/members/{user_id} | Update a workspace member&#39;s role


# **add_workspace_member**
> WorkspaceMemberRecord add_workspace_member(workspace_id, workspace_member_add_request)

Add a member to a workspace

Grants a user membership in the specified workspace with the given role.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.workspace_member_add_request import WorkspaceMemberAddRequest
from aqueduct_sdk.models.workspace_member_record import WorkspaceMemberRecord
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_member_add_request = aqueduct_sdk.WorkspaceMemberAddRequest() # WorkspaceMemberAddRequest | 

    try:
        # Add a member to a workspace
        api_response = await api_instance.add_workspace_member(workspace_id, workspace_member_add_request)
        print("The response of CollaborationApi->add_workspace_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->add_workspace_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_member_add_request** | [**WorkspaceMemberAddRequest**](WorkspaceMemberAddRequest.md)|  | 

### Return type

[**WorkspaceMemberRecord**](WorkspaceMemberRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Member added. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_annotation**
> AnnotationRecord create_annotation(conversation_id, turn_index, annotation_request)

Create an annotation on a conversation turn

Attaches a comment to a specific turn (zero-based index) in a conversation.
The body may contain @mention tokens (e.g. @alice) which trigger asynchronous
in-app notifications and emit `mention` activity records.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.annotation_record import AnnotationRecord
from aqueduct_sdk.models.annotation_request import AnnotationRequest
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    turn_index = 56 # int | 
    annotation_request = aqueduct_sdk.AnnotationRequest() # AnnotationRequest | 

    try:
        # Create an annotation on a conversation turn
        api_response = await api_instance.create_annotation(conversation_id, turn_index, annotation_request)
        print("The response of CollaborationApi->create_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->create_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **turn_index** | **int**|  | 
 **annotation_request** | [**AnnotationRequest**](AnnotationRequest.md)|  | 

### Return type

[**AnnotationRecord**](AnnotationRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Annotation created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_annotation**
> delete_annotation(conversation_id, turn_index, annotation_id)

Delete an annotation

Permanently removes an annotation.

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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    turn_index = 56 # int | 
    annotation_id = 'annotation_id_example' # str | 

    try:
        # Delete an annotation
        await api_instance.delete_annotation(conversation_id, turn_index, annotation_id)
    except Exception as e:
        print("Exception when calling CollaborationApi->delete_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **turn_index** | **int**|  | 
 **annotation_id** | **str**|  | 

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
**204** | Annotation deleted. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_annotations**
> AnnotationListResponse list_annotations(conversation_id, turn_index)

List annotations for a conversation turn

Returns all annotations for the specified turn, ordered by creation time.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.annotation_list_response import AnnotationListResponse
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    turn_index = 56 # int | 

    try:
        # List annotations for a conversation turn
        api_response = await api_instance.list_annotations(conversation_id, turn_index)
        print("The response of CollaborationApi->list_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->list_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **turn_index** | **int**|  | 

### Return type

[**AnnotationListResponse**](AnnotationListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Annotation list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collab_activity**
> CollabActivityListResponse list_collab_activity(type_filter=type_filter, actor=actor, var_from=var_from, to=to, cursor=cursor, page_size=page_size)

List collaboration activity records

Returns a cursor-paginated feed of collaboration activity events for the
authenticated tenant: shares, annotations, mentions, and workspace membership
changes. Scoped to the caller's tenant_id from the JWT claim.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.collab_activity_list_response import CollabActivityListResponse
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    type_filter = 'type_filter_example' # str | Filter by activity type. (optional)
    actor = 'actor_example' # str | Filter by actor user ID. (optional)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Start time (RFC 3339). (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | End time (RFC 3339). (optional)
    cursor = 'cursor_example' # str | Opaque pagination cursor from a previous response. (optional)
    page_size = 50 # int | Number of records to return (default 50, max 200). (optional) (default to 50)

    try:
        # List collaboration activity records
        api_response = await api_instance.list_collab_activity(type_filter=type_filter, actor=actor, var_from=var_from, to=to, cursor=cursor, page_size=page_size)
        print("The response of CollaborationApi->list_collab_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->list_collab_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_filter** | **str**| Filter by activity type. | [optional] 
 **actor** | **str**| Filter by actor user ID. | [optional] 
 **var_from** | **datetime**| Start time (RFC 3339). | [optional] 
 **to** | **datetime**| End time (RFC 3339). | [optional] 
 **cursor** | **str**| Opaque pagination cursor from a previous response. | [optional] 
 **page_size** | **int**| Number of records to return (default 50, max 200). | [optional] [default to 50]

### Return type

[**CollabActivityListResponse**](CollabActivityListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Activity records. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversation_shares**
> ShareListResponse list_conversation_shares(conversation_id)

List shares for a conversation

Returns all active shares for the specified conversation.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.share_list_response import ShareListResponse
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 

    try:
        # List shares for a conversation
        api_response = await api_instance.list_conversation_shares(conversation_id)
        print("The response of CollaborationApi->list_conversation_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->list_conversation_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 

### Return type

[**ShareListResponse**](ShareListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Share list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_presence**
> PresenceListResponse list_presence(workspace_id=workspace_id)

List active presence records for a conversation

Returns the current presence state for all users active in the specified
conversation. Used by the client to restore presence state after a WebSocket
reconnect without replaying the full event stream.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.presence_list_response import PresenceListResponse
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    workspace_id = 'workspace_id_example' # str | Filter presence records to the specified workspace. Omit to return all tenant-scoped records. (optional)

    try:
        # List active presence records for a conversation
        api_response = await api_instance.list_presence(workspace_id=workspace_id)
        print("The response of CollaborationApi->list_presence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->list_presence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Filter presence records to the specified workspace. Omit to return all tenant-scoped records. | [optional] 

### Return type

[**PresenceListResponse**](PresenceListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active presence records. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**503** | Collaboration service unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workspace_members**
> WorkspaceMemberListResponse list_workspace_members(workspace_id)

List workspace members

Returns all current members of the specified workspace.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.workspace_member_list_response import WorkspaceMemberListResponse
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # List workspace members
        api_response = await api_instance.list_workspace_members(workspace_id)
        print("The response of CollaborationApi->list_workspace_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->list_workspace_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceMemberListResponse**](WorkspaceMemberListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member list. |  * X-Trace-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presence_web_socket**
> presence_web_socket(seq=seq)

Subscribe to real-time presence events via WebSocket

Upgrades the connection to a WebSocket and streams presence change events
for the caller's tenant. Events are replayed from `seq` on reconnect for
at-least-once delivery. The server closes the connection on tenant stream
failure with code 1011 (Internal Error).


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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    seq = 0 # int | Replay events after this sequence number (0 = full stream from the beginning). (optional) (default to 0)

    try:
        # Subscribe to real-time presence events via WebSocket
        await api_instance.presence_web_socket(seq=seq)
    except Exception as e:
        print("Exception when calling CollaborationApi->presence_web_socket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seq** | **int**| Replay events after this sequence number (0 &#x3D; full stream from the beginning). | [optional] [default to 0]

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
**101** | Switching Protocols — WebSocket connection established. |  -  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workspace_member**
> remove_workspace_member(workspace_id, user_id)

Remove a member from a workspace

Revokes a user's membership in the specified workspace.

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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove a member from a workspace
        await api_instance.remove_workspace_member(workspace_id, user_id)
    except Exception as e:
        print("Exception when calling CollaborationApi->remove_workspace_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **user_id** | **str**|  | 

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
**204** | Member removed. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_conversation_share**
> revoke_conversation_share(conversation_id, share_id)

Revoke a share

Deletes the share record and removes the associated ABAC policy.

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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    share_id = 'share_id_example' # str | 

    try:
        # Revoke a share
        await api_instance.revoke_conversation_share(conversation_id, share_id)
    except Exception as e:
        print("Exception when calling CollaborationApi->revoke_conversation_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **share_id** | **str**|  | 

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
**204** | Share revoked. |  -  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_conversation**
> ShareRecord share_conversation(conversation_id, share_request)

Share a conversation with a user, role, or team

Creates an ABAC share record granting the specified target read/comment/edit
access to a conversation. Exactly one of target_user_id, target_role_id, or
target_team_id must be set. Bastion ABAC authorization is checked for the
caller before the share is created (fail-closed).


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.share_record import ShareRecord
from aqueduct_sdk.models.share_request import ShareRequest
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    share_request = aqueduct_sdk.ShareRequest() # ShareRequest | 

    try:
        # Share a conversation with a user, role, or team
        api_response = await api_instance.share_conversation(conversation_id, share_request)
        print("The response of CollaborationApi->share_conversation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->share_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **share_request** | [**ShareRequest**](ShareRequest.md)|  | 

### Return type

[**ShareRecord**](ShareRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Share created. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_annotation**
> AnnotationRecord update_annotation(conversation_id, turn_index, annotation_id, annotation_update_request)

Update an annotation body

Updates the body of an existing annotation. Only the original author may
update their annotation — other callers receive 403.


### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.annotation_record import AnnotationRecord
from aqueduct_sdk.models.annotation_update_request import AnnotationUpdateRequest
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    conversation_id = 'conversation_id_example' # str | 
    turn_index = 56 # int | 
    annotation_id = 'annotation_id_example' # str | 
    annotation_update_request = aqueduct_sdk.AnnotationUpdateRequest() # AnnotationUpdateRequest | 

    try:
        # Update an annotation body
        api_response = await api_instance.update_annotation(conversation_id, turn_index, annotation_id, annotation_update_request)
        print("The response of CollaborationApi->update_annotation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->update_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | 
 **turn_index** | **int**|  | 
 **annotation_id** | **str**|  | 
 **annotation_update_request** | [**AnnotationUpdateRequest**](AnnotationUpdateRequest.md)|  | 

### Return type

[**AnnotationRecord**](AnnotationRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated annotation. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace_member_role**
> WorkspaceMemberRecord update_workspace_member_role(workspace_id, user_id, workspace_member_update_request)

Update a workspace member's role

Changes the role of an existing workspace member.

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import aqueduct_sdk
from aqueduct_sdk.models.workspace_member_record import WorkspaceMemberRecord
from aqueduct_sdk.models.workspace_member_update_request import WorkspaceMemberUpdateRequest
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
    api_instance = aqueduct_sdk.CollaborationApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    user_id = 'user_id_example' # str | 
    workspace_member_update_request = aqueduct_sdk.WorkspaceMemberUpdateRequest() # WorkspaceMemberUpdateRequest | 

    try:
        # Update a workspace member's role
        api_response = await api_instance.update_workspace_member_role(workspace_id, user_id, workspace_member_update_request)
        print("The response of CollaborationApi->update_workspace_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaborationApi->update_workspace_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **user_id** | **str**|  | 
 **workspace_member_update_request** | [**WorkspaceMemberUpdateRequest**](WorkspaceMemberUpdateRequest.md)|  | 

### Return type

[**WorkspaceMemberRecord**](WorkspaceMemberRecord.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated member record. |  * X-Trace-ID -  <br>  |
**400** | Validation error (ERR-API-001-003). Request body or parameters failed validation. The &#x60;errors&#x60; array contains field-level details.  |  * API-Version -  <br>  * X-Trace-ID -  <br>  * X-Request-ID -  <br>  |
**401** | Authentication failed. Possible causes: - Token expired (ERR-API-001-002) - Invalid credentials (ERR-API-001-006) - Invalid token signature (ERR-API-001-007)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**403** | Access denied. Possible causes: - Cross-tenant access attempt (ERR-API-001-005) - Insufficient permissions (ERR-API-001-008)  |  * API-Version -  <br>  * X-Trace-ID -  <br>  |
**404** | Resource not found (ERR-API-001-004). |  * API-Version -  <br>  * X-Trace-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

