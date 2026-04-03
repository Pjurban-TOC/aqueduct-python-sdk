# DeleteTenantRequest

Request body for tenant deletion. Matches `tenants.go:102` DeleteTenantRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation** | **str** | Must be the tenant slug to confirm deletion. | 
**reason** | **str** | Reason for deleting the tenant. | 
**export_data** | **bool** | Whether to export tenant data before deletion. | [optional] [default to False]

## Example

```python
from aqueduct_sdk.models.delete_tenant_request import DeleteTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTenantRequest from a JSON string
delete_tenant_request_instance = DeleteTenantRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteTenantRequest.to_json())

# convert the object into a dict
delete_tenant_request_dict = delete_tenant_request_instance.to_dict()
# create an instance of DeleteTenantRequest from a dict
delete_tenant_request_from_dict = DeleteTenantRequest.from_dict(delete_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


