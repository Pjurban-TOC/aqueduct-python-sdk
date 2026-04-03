# ChatMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Message role. | 
**content** | [**ChatMessageContent**](ChatMessageContent.md) |  | 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) | Tool calls made by the assistant. | [optional] 
**tool_call_id** | **str** | ID of the tool call this message is responding to (for role&#x3D;tool). | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


