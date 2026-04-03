# AddDomainResponse

Response for adding a custom domain with verification instructions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**domain** | **str** |  | 
**type** | **str** |  | 
**status** | **str** | Domain status (pending_verification, verified, active, removing). | 
**verification** | [**VerificationDetails**](VerificationDetails.md) |  | 
**created_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.add_domain_response import AddDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainResponse from a JSON string
add_domain_response_instance = AddDomainResponse.from_json(json)
# print the JSON string representation of the object
print(AddDomainResponse.to_json())

# convert the object into a dict
add_domain_response_dict = add_domain_response_instance.to_dict()
# create an instance of AddDomainResponse from a dict
add_domain_response_from_dict = AddDomainResponse.from_dict(add_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


