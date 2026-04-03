# SetTenantsRequest

Request body for configuring which tenants are monitored by the compliance scheduler. Matches compliance-engine SetTenantsRequest struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_ids** | **List[str]** | List of tenant identifiers to monitor for compliance. | 

## Example

```python
from aqueduct_sdk.models.set_tenants_request import SetTenantsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetTenantsRequest from a JSON string
set_tenants_request_instance = SetTenantsRequest.from_json(json)
# print the JSON string representation of the object
print(SetTenantsRequest.to_json())

# convert the object into a dict
set_tenants_request_dict = set_tenants_request_instance.to_dict()
# create an instance of SetTenantsRequest from a dict
set_tenants_request_from_dict = SetTenantsRequest.from_dict(set_tenants_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


