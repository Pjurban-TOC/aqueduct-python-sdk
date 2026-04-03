# ListTenantsResponse

Paginated tenant list. Matches `tenants.go:134` ListTenantsResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[TenantResponse]**](TenantResponse.md) |  | 
**next_cursor** | **str** | Cursor for the next page. Empty when no more results. | [optional] 
**total** | **int** | Total number of tenants matching the query. | 

## Example

```python
from aqueduct_sdk.models.list_tenants_response import ListTenantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTenantsResponse from a JSON string
list_tenants_response_instance = ListTenantsResponse.from_json(json)
# print the JSON string representation of the object
print(ListTenantsResponse.to_json())

# convert the object into a dict
list_tenants_response_dict = list_tenants_response_instance.to_dict()
# create an instance of ListTenantsResponse from a dict
list_tenants_response_from_dict = ListTenantsResponse.from_dict(list_tenants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


