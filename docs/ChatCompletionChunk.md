# ChatCompletionChunk

Streaming chat completion chunk. Sent as Server-Sent Events with content-type `text/event-stream`. Uses `delta` instead of `message`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **int** |  | 
**model** | **str** |  | 
**choices** | [**List[ChatCompletionChunkChoicesInner]**](ChatCompletionChunkChoicesInner.md) |  | 
**usage** | [**CompletionUsage**](CompletionUsage.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_chunk import ChatCompletionChunk

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionChunk from a JSON string
chat_completion_chunk_instance = ChatCompletionChunk.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionChunk.to_json())

# convert the object into a dict
chat_completion_chunk_dict = chat_completion_chunk_instance.to_dict()
# create an instance of ChatCompletionChunk from a dict
chat_completion_chunk_from_dict = ChatCompletionChunk.from_dict(chat_completion_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


