# DomainListItem

Domain summary in list responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**domain** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**ssl_expires_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.domain_list_item import DomainListItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainListItem from a JSON string
domain_list_item_instance = DomainListItem.from_json(json)
# print the JSON string representation of the object
print(DomainListItem.to_json())

# convert the object into a dict
domain_list_item_dict = domain_list_item_instance.to_dict()
# create an instance of DomainListItem from a dict
domain_list_item_from_dict = DomainListItem.from_dict(domain_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


