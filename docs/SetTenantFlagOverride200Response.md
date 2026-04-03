# SetTenantFlagOverride200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**flag** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.set_tenant_flag_override200_response import SetTenantFlagOverride200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetTenantFlagOverride200Response from a JSON string
set_tenant_flag_override200_response_instance = SetTenantFlagOverride200Response.from_json(json)
# print the JSON string representation of the object
print(SetTenantFlagOverride200Response.to_json())

# convert the object into a dict
set_tenant_flag_override200_response_dict = set_tenant_flag_override200_response_instance.to_dict()
# create an instance of SetTenantFlagOverride200Response from a dict
set_tenant_flag_override200_response_from_dict = SetTenantFlagOverride200Response.from_dict(set_tenant_flag_override200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


