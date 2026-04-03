# VerifyDomainResponse

Response for manual domain verification (API-PLAT-004-05).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 
**verification_status** | **str** | Current verification state (pending, verified, failed). | 
**dns_record_found** | **bool** |  | 
**last_checked_at** | **datetime** |  | 
**next_check_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.verify_domain_response import VerifyDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDomainResponse from a JSON string
verify_domain_response_instance = VerifyDomainResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyDomainResponse.to_json())

# convert the object into a dict
verify_domain_response_dict = verify_domain_response_instance.to_dict()
# create an instance of VerifyDomainResponse from a dict
verify_domain_response_from_dict = VerifyDomainResponse.from_dict(verify_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


