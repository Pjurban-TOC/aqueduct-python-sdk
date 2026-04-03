# ChatMessageContentOneOfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**image_url** | [**ChatMessageContentOneOfInnerImageUrl**](ChatMessageContentOneOfInnerImageUrl.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_message_content_one_of_inner import ChatMessageContentOneOfInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageContentOneOfInner from a JSON string
chat_message_content_one_of_inner_instance = ChatMessageContentOneOfInner.from_json(json)
# print the JSON string representation of the object
print(ChatMessageContentOneOfInner.to_json())

# convert the object into a dict
chat_message_content_one_of_inner_dict = chat_message_content_one_of_inner_instance.to_dict()
# create an instance of ChatMessageContentOneOfInner from a dict
chat_message_content_one_of_inner_from_dict = ChatMessageContentOneOfInner.from_dict(chat_message_content_one_of_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


