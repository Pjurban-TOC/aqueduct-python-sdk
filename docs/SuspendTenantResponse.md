# SuspendTenantResponse

Response confirming tenant suspension with computed timeline dates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Identifier of the suspended tenant. | 
**status** | **str** | New tenant lifecycle status after suspension. | 
**suspended_at** | **datetime** | Timestamp when the suspension took effect. | 
**grace_period_ends** | **datetime** | Timestamp when the grace period expires. | 
**deletion_eligible_at** | **datetime** | Earliest date the tenant can be permanently deleted. | 

## Example

```python
from aqueduct_sdk.models.suspend_tenant_response import SuspendTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendTenantResponse from a JSON string
suspend_tenant_response_instance = SuspendTenantResponse.from_json(json)
# print the JSON string representation of the object
print(SuspendTenantResponse.to_json())

# convert the object into a dict
suspend_tenant_response_dict = suspend_tenant_response_instance.to_dict()
# create an instance of SuspendTenantResponse from a dict
suspend_tenant_response_from_dict = SuspendTenantResponse.from_dict(suspend_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


