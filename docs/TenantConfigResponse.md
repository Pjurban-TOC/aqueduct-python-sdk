# TenantConfigResponse

Tenant configuration in responses. Matches `tenants.go:81` TenantConfigResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_timeout_minutes** | **int** |  | [optional] 
**mfa_required** | **bool** |  | [optional] 
**ip_allowlist** | **List[str]** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.tenant_config_response import TenantConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConfigResponse from a JSON string
tenant_config_response_instance = TenantConfigResponse.from_json(json)
# print the JSON string representation of the object
print(TenantConfigResponse.to_json())

# convert the object into a dict
tenant_config_response_dict = tenant_config_response_instance.to_dict()
# create an instance of TenantConfigResponse from a dict
tenant_config_response_from_dict = TenantConfigResponse.from_dict(tenant_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


