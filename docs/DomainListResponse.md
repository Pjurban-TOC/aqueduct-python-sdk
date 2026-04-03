# DomainListResponse

List of domains for a tenant (API-PLAT-004-03).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[DomainListItem]**](DomainListItem.md) |  | 

## Example

```python
from aqueduct_sdk.models.domain_list_response import DomainListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainListResponse from a JSON string
domain_list_response_instance = DomainListResponse.from_json(json)
# print the JSON string representation of the object
print(DomainListResponse.to_json())

# convert the object into a dict
domain_list_response_dict = domain_list_response_instance.to_dict()
# create an instance of DomainListResponse from a dict
domain_list_response_from_dict = DomainListResponse.from_dict(domain_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


