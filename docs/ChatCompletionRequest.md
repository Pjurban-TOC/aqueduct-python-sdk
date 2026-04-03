# ChatCompletionRequest

OpenAI-compatible chat completion request. This is the universal interchange format for AI gateway inference endpoints (2024-2026). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Model identifier. May be a canonical name (e.g., &#x60;gpt-4o&#x60;) or a routing alias configured per-tenant. | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) | Conversation messages in chronological order. | 
**temperature** | **float** | Sampling temperature. | [optional] [default to 1]
**top_p** | **float** | Nucleus sampling parameter. | [optional] [default to 1]
**max_tokens** | **int** | Maximum tokens to generate. | [optional] 
**stream** | **bool** | If true, returns a stream of &#x60;ChatCompletionChunk&#x60; objects via Server-Sent Events (SSE) with content-type &#x60;text/event-stream&#x60;.  | [optional] [default to False]
**stop** | [**ChatCompletionRequestStop**](ChatCompletionRequestStop.md) |  | [optional] 
**frequency_penalty** | **float** | Frequency penalty for token repetition. | [optional] [default to 0]
**presence_penalty** | **float** | Presence penalty for new topic encouragement. | [optional] [default to 0]
**response_format** | [**ChatCompletionRequestResponseFormat**](ChatCompletionRequestResponseFormat.md) |  | [optional] 
**tools** | [**List[ToolDefinition]**](ToolDefinition.md) | Available tool definitions for function calling. | [optional] 
**tool_choice** | [**ChatCompletionRequestToolChoice**](ChatCompletionRequestToolChoice.md) |  | [optional] 
**user** | **str** | End-user identifier for abuse monitoring. | [optional] 
**x_aqueduct_priority** | **str** | Request priority for scheduling. Per DLPM [arXiv:2501.14312]. | [optional] [default to 'normal']

## Example

```python
from aqueduct_sdk.models.chat_completion_request import ChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequest from a JSON string
chat_completion_request_instance = ChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequest.to_json())

# convert the object into a dict
chat_completion_request_dict = chat_completion_request_instance.to_dict()
# create an instance of ChatCompletionRequest from a dict
chat_completion_request_from_dict = ChatCompletionRequest.from_dict(chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


