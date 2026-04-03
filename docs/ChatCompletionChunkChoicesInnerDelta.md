# ChatCompletionChunkChoicesInnerDelta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_chunk_choices_inner_delta import ChatCompletionChunkChoicesInnerDelta

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionChunkChoicesInnerDelta from a JSON string
chat_completion_chunk_choices_inner_delta_instance = ChatCompletionChunkChoicesInnerDelta.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionChunkChoicesInnerDelta.to_json())

# convert the object into a dict
chat_completion_chunk_choices_inner_delta_dict = chat_completion_chunk_choices_inner_delta_instance.to_dict()
# create an instance of ChatCompletionChunkChoicesInnerDelta from a dict
chat_completion_chunk_choices_inner_delta_from_dict = ChatCompletionChunkChoicesInnerDelta.from_dict(chat_completion_chunk_choices_inner_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


