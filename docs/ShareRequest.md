# ShareRequest

Request body for sharing a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_user_id** | **str** | Grant access to a specific user. | [optional] 
**target_role_id** | **str** | Grant access to all users with this role. | [optional] 
**target_team_id** | **str** | Grant access to all members of this team. | [optional] 
**permissions** | **List[str]** |  | 
**expires_at** | **datetime** | Optional expiry timestamp. | [optional] 

## Example

```python
from aqueduct_sdk.models.share_request import ShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareRequest from a JSON string
share_request_instance = ShareRequest.from_json(json)
# print the JSON string representation of the object
print(ShareRequest.to_json())

# convert the object into a dict
share_request_dict = share_request_instance.to_dict()
# create an instance of ShareRequest from a dict
share_request_from_dict = ShareRequest.from_dict(share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


