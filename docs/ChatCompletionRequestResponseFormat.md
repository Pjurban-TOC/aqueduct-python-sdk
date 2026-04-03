# ChatCompletionRequestResponseFormat

Desired response format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**json_schema** | **object** | JSON Schema when type is &#x60;json_schema&#x60;. | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_request_response_format import ChatCompletionRequestResponseFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionRequestResponseFormat from a JSON string
chat_completion_request_response_format_instance = ChatCompletionRequestResponseFormat.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionRequestResponseFormat.to_json())

# convert the object into a dict
chat_completion_request_response_format_dict = chat_completion_request_response_format_instance.to_dict()
# create an instance of ChatCompletionRequestResponseFormat from a dict
chat_completion_request_response_format_from_dict = ChatCompletionRequestResponseFormat.from_dict(chat_completion_request_response_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


