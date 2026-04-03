# WorkspaceMemberListResponse

List of workspace members.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[WorkspaceMemberRecord]**](WorkspaceMemberRecord.md) |  | 

## Example

```python
from aqueduct_sdk.models.workspace_member_list_response import WorkspaceMemberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberListResponse from a JSON string
workspace_member_list_response_instance = WorkspaceMemberListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberListResponse.to_json())

# convert the object into a dict
workspace_member_list_response_dict = workspace_member_list_response_instance.to_dict()
# create an instance of WorkspaceMemberListResponse from a dict
workspace_member_list_response_from_dict = WorkspaceMemberListResponse.from_dict(workspace_member_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


