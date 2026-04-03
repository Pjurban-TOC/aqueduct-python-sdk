# ChatMessageContent

Message content (string or structured content parts).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aqueduct_sdk.models.chat_message_content import ChatMessageContent

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageContent from a JSON string
chat_message_content_instance = ChatMessageContent.from_json(json)
# print the JSON string representation of the object
print(ChatMessageContent.to_json())

# convert the object into a dict
chat_message_content_dict = chat_message_content_instance.to_dict()
# create an instance of ChatMessageContent from a dict
chat_message_content_from_dict = ChatMessageContent.from_dict(chat_message_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


