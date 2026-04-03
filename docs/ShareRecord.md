# ShareRecord

Access share granting a user, role, or team access to a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Share identifier (UUID v4). | 
**tenant_id** | **str** |  | 
**conversation_id** | **str** |  | 
**shared_by** | **str** | User ID of the user who created the share. | 
**target_user_id** | **str** | Target individual user (mutually exclusive with target_role_id / target_team_id). | [optional] 
**target_role_id** | **str** | Target role (mutually exclusive with target_user_id / target_team_id). | [optional] 
**target_team_id** | **str** | Target team (mutually exclusive with target_user_id / target_role_id). | [optional] 
**permissions** | **List[str]** | Granted permission scopes. | 
**expires_at** | **datetime** | Optional share expiry. Omit or set to zero for no expiry. | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.share_record import ShareRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ShareRecord from a JSON string
share_record_instance = ShareRecord.from_json(json)
# print the JSON string representation of the object
print(ShareRecord.to_json())

# convert the object into a dict
share_record_dict = share_record_instance.to_dict()
# create an instance of ShareRecord from a dict
share_record_from_dict = ShareRecord.from_dict(share_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


