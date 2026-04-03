# SetTenantConfigOverride200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.set_tenant_config_override200_response import SetTenantConfigOverride200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetTenantConfigOverride200Response from a JSON string
set_tenant_config_override200_response_instance = SetTenantConfigOverride200Response.from_json(json)
# print the JSON string representation of the object
print(SetTenantConfigOverride200Response.to_json())

# convert the object into a dict
set_tenant_config_override200_response_dict = set_tenant_config_override200_response_instance.to_dict()
# create an instance of SetTenantConfigOverride200Response from a dict
set_tenant_config_override200_response_from_dict = SetTenantConfigOverride200Response.from_dict(set_tenant_config_override200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


