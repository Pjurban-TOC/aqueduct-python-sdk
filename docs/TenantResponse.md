# TenantResponse

Tenant in API responses. Matches `tenants.go:67` TenantResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Unique tenant identifier. | 
**name** | **str** |  | 
**slug** | **str** |  | 
**tier** | [**TenantTier**](TenantTier.md) |  | 
**region** | **str** |  | 
**status** | [**TenantStatus**](TenantStatus.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**config** | [**TenantConfigResponse**](TenantConfigResponse.md) |  | [optional] 
**usage_summary** | [**UsageSummaryResponse**](UsageSummaryResponse.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.tenant_response import TenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantResponse from a JSON string
tenant_response_instance = TenantResponse.from_json(json)
# print the JSON string representation of the object
print(TenantResponse.to_json())

# convert the object into a dict
tenant_response_dict = tenant_response_instance.to_dict()
# create an instance of TenantResponse from a dict
tenant_response_from_dict = TenantResponse.from_dict(tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


