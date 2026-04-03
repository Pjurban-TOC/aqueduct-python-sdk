# ChatCompletionRequestToolChoice

Tool selection strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**function** | [**ChatCompletionRequestToolChoiceOneOfFunction**](ChatCompletionRequestToolChoiceOneOfFunction.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_request_tool_choice import ChatCompletionRequestToolChoice

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestToolChoice from a JSON string
chat_completion_request_tool_choice_instance = ChatCompletionRequestToolChoice.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestToolChoice.to_json())

# convert the object into a dict
chat_completion_request_tool_choice_dict = chat_completion_request_tool_choice_instance.to_dict()
# create an instance of ChatCompletionRequestToolChoice from a dict
chat_completion_request_tool_choice_from_dict = ChatCompletionRequestToolChoice.from_dict(chat_completion_request_tool_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


