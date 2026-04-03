# StatusUpdateResponse

Response for tenant status update. Matches `tenants.go:124` StatusUpdateResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**from_status** | **str** |  | 
**to_status** | **str** |  | 
**reason** | **str** |  | 
**changed_at** | **datetime** |  | 
**changed_by** | **str** | User ID of the administrator who made the change. | 

## Example

```python
from aqueduct_sdk.models.status_update_response import StatusUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusUpdateResponse from a JSON string
status_update_response_instance = StatusUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(StatusUpdateResponse.to_json())

# convert the object into a dict
status_update_response_dict = status_update_response_instance.to_dict()
# create an instance of StatusUpdateResponse from a dict
status_update_response_from_dict = StatusUpdateResponse.from_dict(status_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


