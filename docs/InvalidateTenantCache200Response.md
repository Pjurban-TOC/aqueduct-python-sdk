# InvalidateTenantCache200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**invalidated_count** | **int** |  | [optional] 
**duration_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.invalidate_tenant_cache200_response import InvalidateTenantCache200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateTenantCache200Response from a JSON string
invalidate_tenant_cache200_response_instance = InvalidateTenantCache200Response.from_json(json)
# print the JSON string representation of the object
print(InvalidateTenantCache200Response.to_json())

# convert the object into a dict
invalidate_tenant_cache200_response_dict = invalidate_tenant_cache200_response_instance.to_dict()
# create an instance of InvalidateTenantCache200Response from a dict
invalidate_tenant_cache200_response_from_dict = InvalidateTenantCache200Response.from_dict(invalidate_tenant_cache200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


