# TenantConfigRequest

Tenant configuration in requests. Matches `tenants.go:60` TenantConfigRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_timeout_minutes** | **int** | Session timeout in minutes. | [optional] 
**mfa_required** | **bool** | Whether MFA is required for all users in this tenant. | [optional] 
**ip_allowlist** | **List[str]** | CIDR blocks allowed to access this tenant&#39;s resources. | [optional] 

## Example

```python
from aqueduct_sdk.models.tenant_config_request import TenantConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfigRequest from a JSON string
tenant_config_request_instance = TenantConfigRequest.from_json(json)
# print the JSON string representation of the object
print(TenantConfigRequest.to_json())

# convert the object into a dict
tenant_config_request_dict = tenant_config_request_instance.to_dict()
# create an instance of TenantConfigRequest from a dict
tenant_config_request_from_dict = TenantConfigRequest.from_dict(tenant_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


