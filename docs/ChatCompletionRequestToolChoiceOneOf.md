# ChatCompletionRequestToolChoiceOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**function** | [**ChatCompletionRequestToolChoiceOneOfFunction**](ChatCompletionRequestToolChoiceOneOfFunction.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_request_tool_choice_one_of import ChatCompletionRequestToolChoiceOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestToolChoiceOneOf from a JSON string
chat_completion_request_tool_choice_one_of_instance = ChatCompletionRequestToolChoiceOneOf.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestToolChoiceOneOf.to_json())

# convert the object into a dict
chat_completion_request_tool_choice_one_of_dict = chat_completion_request_tool_choice_one_of_instance.to_dict()
# create an instance of ChatCompletionRequestToolChoiceOneOf from a dict
chat_completion_request_tool_choice_one_of_from_dict = ChatCompletionRequestToolChoiceOneOf.from_dict(chat_completion_request_tool_choice_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


