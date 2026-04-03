# CreateTenantRequest

Request body for creating a new tenant. Matches `tenants.go:50` CreateTenantRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable tenant name. | 
**slug** | **str** | URL-safe tenant slug. Must match &#x60;^[a-z0-9][a-z0-9-]{1,48}[a-z0-9]$&#x60;. | 
**tier** | [**TenantTier**](TenantTier.md) |  | 
**region** | **str** | Deployment region for data residency. | 
**admin_email** | **str** | Email address for the initial tenant administrator. | 
**config** | [**TenantConfigRequest**](TenantConfigRequest.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.create_tenant_request import CreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantRequest from a JSON string
create_tenant_request_instance = CreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantRequest.to_json())

# convert the object into a dict
create_tenant_request_dict = create_tenant_request_instance.to_dict()
# create an instance of CreateTenantRequest from a dict
create_tenant_request_from_dict = CreateTenantRequest.from_dict(create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


