# CollabActivityRecord

Collaboration activity event (share, annotation, mention, workspace membership change).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Activity record identifier (UUID v4). | 
**tenant_id** | **str** |  | 
**actor_user_id** | **str** |  | 
**type** | **str** | Activity event type. | 
**resource_id** | **str** |  | 
**resource_type** | **str** |  | 
**metadata** | **Dict[str, str]** | Event-specific metadata (e.g. annotation_id, share_id, mentioned_user). | [optional] 
**occurred_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.collab_activity_record import CollabActivityRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CollabActivityRecord from a JSON string
collab_activity_record_instance = CollabActivityRecord.from_json(json)
# print the JSON string representation of the object
print(CollabActivityRecord.to_json())

# convert the object into a dict
collab_activity_record_dict = collab_activity_record_instance.to_dict()
# create an instance of CollabActivityRecord from a dict
collab_activity_record_from_dict = CollabActivityRecord.from_dict(collab_activity_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


