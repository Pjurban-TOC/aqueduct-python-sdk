# ReactivateTenantRequest

Request body for reactivating a suspended tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for reactivation (e.g., payment received, investigation cleared). | 
**waive_outstanding_balance** | **bool** | When true, outstanding balance is waived as part of reactivation. | [optional] 

## Example

```python
from aqueduct_sdk.models.reactivate_tenant_request import ReactivateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReactivateTenantRequest from a JSON string
reactivate_tenant_request_instance = ReactivateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(ReactivateTenantRequest.to_json())

# convert the object into a dict
reactivate_tenant_request_dict = reactivate_tenant_request_instance.to_dict()
# create an instance of ReactivateTenantRequest from a dict
reactivate_tenant_request_from_dict = ReactivateTenantRequest.from_dict(reactivate_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


