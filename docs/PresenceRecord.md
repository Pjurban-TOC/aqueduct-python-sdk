# PresenceRecord

Real-time presence state for a user in a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Presence record identifier (UUID v4). | 
**tenant_id** | **str** |  | 
**conversation_id** | **str** |  | 
**user_id** | **str** |  | 
**status** | **str** | Presence status. | 
**cursor_position** | **int** | Character offset cursor position within the conversation (optional). | [optional] 
**seq** | **int** | Monotonic sequence number for ordering events. | 
**last_seen_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.presence_record import PresenceRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PresenceRecord from a JSON string
presence_record_instance = PresenceRecord.from_json(json)
# print the JSON string representation of the object
print(PresenceRecord.to_json())

# convert the object into a dict
presence_record_dict = presence_record_instance.to_dict()
# create an instance of PresenceRecord from a dict
presence_record_from_dict = PresenceRecord.from_dict(presence_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


