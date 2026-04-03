# DomainResponse

Detailed domain information (API-PLAT-004-02).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**domain** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**is_apex** | **bool** | Whether this is an apex (root) domain. | 
**verification** | [**VerificationStatus**](VerificationStatus.md) |  | [optional] 
**ssl** | [**SSLStatus**](SSLStatus.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.domain_response import DomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponse from a JSON string
domain_response_instance = DomainResponse.from_json(json)
# print the JSON string representation of the object
print(DomainResponse.to_json())

# convert the object into a dict
domain_response_dict = domain_response_instance.to_dict()
# create an instance of DomainResponse from a dict
domain_response_from_dict = DomainResponse.from_dict(domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


