# WorkspaceMemberAddRequest

Request body for adding a workspace member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.workspace_member_add_request import WorkspaceMemberAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberAddRequest from a JSON string
workspace_member_add_request_instance = WorkspaceMemberAddRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberAddRequest.to_json())

# convert the object into a dict
workspace_member_add_request_dict = workspace_member_add_request_instance.to_dict()
# create an instance of WorkspaceMemberAddRequest from a dict
workspace_member_add_request_from_dict = WorkspaceMemberAddRequest.from_dict(workspace_member_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


