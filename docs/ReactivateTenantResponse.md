# ReactivateTenantResponse

Response confirming tenant reactivation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Identifier of the reactivated tenant. | 
**status** | **str** | New tenant lifecycle status after reactivation. | 
**reactivated_at** | **datetime** | Timestamp when the tenant was reactivated. | 
**reactivated_by** | **str** | User ID of the administrator who performed the reactivation. | 

## Example

```python
from aqueduct_sdk.models.reactivate_tenant_response import ReactivateTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReactivateTenantResponse from a JSON string
reactivate_tenant_response_instance = ReactivateTenantResponse.from_json(json)
# print the JSON string representation of the object
print(ReactivateTenantResponse.to_json())

# convert the object into a dict
reactivate_tenant_response_dict = reactivate_tenant_response_instance.to_dict()
# create an instance of ReactivateTenantResponse from a dict
reactivate_tenant_response_from_dict = ReactivateTenantResponse.from_dict(reactivate_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


