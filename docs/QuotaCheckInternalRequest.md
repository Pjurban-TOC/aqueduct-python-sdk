# QuotaCheckInternalRequest

Internal quota check request. Matches `quotas.go:166` QuotaCheckInternalRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**resource** | **str** |  | 
**amount** | **int** |  | [optional] [default to 1]
**model** | **str** | Model being invoked (for model-specific quota checks). | [optional] 
**feature** | **str** | Feature being used (for feature-specific quota checks). | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_check_internal_request import QuotaCheckInternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaCheckInternalRequest from a JSON string
quota_check_internal_request_instance = QuotaCheckInternalRequest.from_json(json)
# print the JSON string representation of the object
print(QuotaCheckInternalRequest.to_json())

# convert the object into a dict
quota_check_internal_request_dict = quota_check_internal_request_instance.to_dict()
# create an instance of QuotaCheckInternalRequest from a dict
quota_check_internal_request_from_dict = QuotaCheckInternalRequest.from_dict(quota_check_internal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


