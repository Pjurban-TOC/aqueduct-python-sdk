# StoredMarking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**dissemination_controls** | **List[str]** |  | [optional] 
**releasable_to** | **List[str]** |  | [optional] 
**controlled_by** | **str** |  | [optional] 
**banner_line** | **str** | Rendered banner marking per DoDI 5200.48. | [optional] 
**accumulo_visibility** | **str** | Ntikuma visibility expression. | [optional] 
**decontrol_date** | **str** |  | [optional] 
**decontrol_event** | **str** |  | [optional] 
**marked_by** | **str** |  | [optional] 
**marked_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.stored_marking import StoredMarking

# TODO update the JSON string below
json = "{}"
# create an instance of StoredMarking from a JSON string
stored_marking_instance = StoredMarking.from_json(json)
# print the JSON string representation of the object
print(StoredMarking.to_json())

# convert the object into a dict
stored_marking_dict = stored_marking_instance.to_dict()
# create an instance of StoredMarking from a dict
stored_marking_from_dict = StoredMarking.from_dict(stored_marking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


