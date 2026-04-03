# WorkspaceMemberUpdateRequest

Request body for updating a member's role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.workspace_member_update_request import WorkspaceMemberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberUpdateRequest from a JSON string
workspace_member_update_request_instance = WorkspaceMemberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberUpdateRequest.to_json())

# convert the object into a dict
workspace_member_update_request_dict = workspace_member_update_request_instance.to_dict()
# create an instance of WorkspaceMemberUpdateRequest from a dict
workspace_member_update_request_from_dict = WorkspaceMemberUpdateRequest.from_dict(workspace_member_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


