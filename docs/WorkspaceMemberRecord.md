# WorkspaceMemberRecord

Workspace membership record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | 
**role** | **str** | Member role within the workspace. | 
**joined_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.workspace_member_record import WorkspaceMemberRecord

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberRecord from a JSON string
workspace_member_record_instance = WorkspaceMemberRecord.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberRecord.to_json())

# convert the object into a dict
workspace_member_record_dict = workspace_member_record_instance.to_dict()
# create an instance of WorkspaceMemberRecord from a dict
workspace_member_record_from_dict = WorkspaceMemberRecord.from_dict(workspace_member_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


