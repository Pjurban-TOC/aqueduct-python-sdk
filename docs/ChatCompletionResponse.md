# ChatCompletionResponse

Non-streaming chat completion response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique completion identifier. | 
**object** | **str** |  | 
**created** | **int** | Unix timestamp of creation. | 
**model** | **str** | Actual model used (may differ from requested if routed). | 
**choices** | [**List[ChatCompletionResponseChoicesInner]**](ChatCompletionResponseChoicesInner.md) |  | 
**usage** | [**CompletionUsage**](CompletionUsage.md) |  | 
**system_fingerprint** | **str** | Backend system configuration fingerprint. | [optional] 
**x_aqueduct_trace_id** | **str** | Distributed trace ID for this request. | [optional] 
**x_aqueduct_tenant_id** | **str** |  | [optional] 
**x_aqueduct_provider** | **str** | Upstream provider that served this request. | [optional] 
**x_aqueduct_cache_status** | **str** | Cache status for this response. Also returned as the &#x60;X-Cache-Status&#x60; response header. HIT &#x3D; served from cache, MISS &#x3D; fresh from provider, BYPASS &#x3D; cache skipped due to X-Cache-Control header.  | [optional] 
**x_aqueduct_dlp_result** | [**ChatCompletionResponseXAqueductDlpResult**](ChatCompletionResponseXAqueductDlpResult.md) |  | [optional] 
**x_aqueduct_routing** | [**ChatCompletionResponseXAqueductRouting**](ChatCompletionResponseXAqueductRouting.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_response import ChatCompletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionResponse from a JSON string
chat_completion_response_instance = ChatCompletionResponse.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionResponse.to_json())

# convert the object into a dict
chat_completion_response_dict = chat_completion_response_instance.to_dict()
# create an instance of ChatCompletionResponse from a dict
chat_completion_response_from_dict = ChatCompletionResponse.from_dict(chat_completion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


