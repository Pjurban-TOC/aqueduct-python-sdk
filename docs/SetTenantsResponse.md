# SetTenantsResponse

Response confirming the tenants configured for compliance monitoring. Matches compliance-engine SetTenantsResponse struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Result status of the set tenants operation. | 
**tenant_ids** | **List[str]** | Tenant identifiers now monitored by the compliance scheduler. | 

## Example

```python
from aqueduct_sdk.models.set_tenants_response import SetTenantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetTenantsResponse from a JSON string
set_tenants_response_instance = SetTenantsResponse.from_json(json)
# print the JSON string representation of the object
print(SetTenantsResponse.to_json())

# convert the object into a dict
set_tenants_response_dict = set_tenants_response_instance.to_dict()
# create an instance of SetTenantsResponse from a dict
set_tenants_response_from_dict = SetTenantsResponse.from_dict(set_tenants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


