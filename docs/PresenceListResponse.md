# PresenceListResponse

List of active presence records for a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[PresenceRecord]**](PresenceRecord.md) |  | 

## Example

```python
from aqueduct_sdk.models.presence_list_response import PresenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PresenceListResponse from a JSON string
presence_list_response_instance = PresenceListResponse.from_json(json)
# print the JSON string representation of the object
print(PresenceListResponse.to_json())

# convert the object into a dict
presence_list_response_dict = presence_list_response_instance.to_dict()
# create an instance of PresenceListResponse from a dict
presence_list_response_from_dict = PresenceListResponse.from_dict(presence_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


