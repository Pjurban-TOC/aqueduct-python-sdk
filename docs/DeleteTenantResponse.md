# DeleteTenantResponse

Response for tenant deletion. Matches `tenants.go:109` DeleteTenantResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**status** | **str** |  | 
**scheduled_for** | **datetime** | When the deletion will be executed (72-hour grace period). | 
**export_requested** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.delete_tenant_response import DeleteTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTenantResponse from a JSON string
delete_tenant_response_instance = DeleteTenantResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteTenantResponse.to_json())

# convert the object into a dict
delete_tenant_response_dict = delete_tenant_response_instance.to_dict()
# create an instance of DeleteTenantResponse from a dict
delete_tenant_response_from_dict = DeleteTenantResponse.from_dict(delete_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


