# SuspendTenantRequest

Request body for suspending a tenant. Matches tenant-service SuspendTenantRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Categorized reason for suspension. | 
**details** | **str** | Human-readable explanation of the suspension reason. | 
**suspension_type** | **str** | Severity of the suspension. \&quot;payment_hold\&quot; restricts writes; \&quot;full_suspension\&quot; blocks all access. | 
**grace_period_days** | **int** | Number of days before the tenant becomes eligible for deletion. | 

## Example

```python
from aqueduct_sdk.models.suspend_tenant_request import SuspendTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendTenantRequest from a JSON string
suspend_tenant_request_instance = SuspendTenantRequest.from_json(json)
# print the JSON string representation of the object
print(SuspendTenantRequest.to_json())

# convert the object into a dict
suspend_tenant_request_dict = suspend_tenant_request_instance.to_dict()
# create an instance of SuspendTenantRequest from a dict
suspend_tenant_request_from_dict = SuspendTenantRequest.from_dict(suspend_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


