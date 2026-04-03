# RemoveDomainResponse

Response for domain removal (API-PLAT-004-04).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**status** | **str** |  | 
**grace_period_ends** | **datetime** |  | 
**fully_removed_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.remove_domain_response import RemoveDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveDomainResponse from a JSON string
remove_domain_response_instance = RemoveDomainResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveDomainResponse.to_json())

# convert the object into a dict
remove_domain_response_dict = remove_domain_response_instance.to_dict()
# create an instance of RemoveDomainResponse from a dict
remove_domain_response_from_dict = RemoveDomainResponse.from_dict(remove_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


