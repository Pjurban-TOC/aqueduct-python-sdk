# QuotaCheckInternalResponse

Internal quota check response. Matches `quotas.go:175` QuotaCheckInternalResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | Whether the request is within quota. | 
**quota_status** | **str** | Current quota status. | 
**current_usage** | **int** |  | 
**limit** | **int** |  | 
**remaining** | **int** |  | 
**reset_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_check_internal_response import QuotaCheckInternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaCheckInternalResponse from a JSON string
quota_check_internal_response_instance = QuotaCheckInternalResponse.from_json(json)
# print the JSON string representation of the object
print(QuotaCheckInternalResponse.to_json())

# convert the object into a dict
quota_check_internal_response_dict = quota_check_internal_response_instance.to_dict()
# create an instance of QuotaCheckInternalResponse from a dict
quota_check_internal_response_from_dict = QuotaCheckInternalResponse.from_dict(quota_check_internal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


