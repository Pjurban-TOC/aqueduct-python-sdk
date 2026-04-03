# DeletionTimeline

Key milestones in the deletion process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**soft_delete_at** | **datetime** | Scheduled soft deletion timestamp. | 
**hard_delete_at** | **datetime** | Scheduled permanent purge timestamp. | 
**completed_at** | **datetime** | Timestamp when deletion completed, or null if still in progress. | [optional] 

## Example

```python
from aqueduct_sdk.models.deletion_timeline import DeletionTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionTimeline from a JSON string
deletion_timeline_instance = DeletionTimeline.from_json(json)
# print the JSON string representation of the object
print(DeletionTimeline.to_json())

# convert the object into a dict
deletion_timeline_dict = deletion_timeline_instance.to_dict()
# create an instance of DeletionTimeline from a dict
deletion_timeline_from_dict = DeletionTimeline.from_dict(deletion_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


