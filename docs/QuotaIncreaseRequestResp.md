# QuotaIncreaseRequestResp

Response for quota increase request. Matches `quotas.go:140` QuotaIncreaseRequestResp.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for tracking this request. | 
**status** | **str** |  | 
**submitted_at** | **datetime** |  | 
**expected_response_time** | **str** | Estimated response time. | 

## Example

```python
from aqueduct_sdk.models.quota_increase_request_resp import QuotaIncreaseRequestResp

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaIncreaseRequestResp from a JSON string
quota_increase_request_resp_instance = QuotaIncreaseRequestResp.from_json(json)
# print the JSON string representation of the object
print(QuotaIncreaseRequestResp.to_json())

# convert the object into a dict
quota_increase_request_resp_dict = quota_increase_request_resp_instance.to_dict()
# create an instance of QuotaIncreaseRequestResp from a dict
quota_increase_request_resp_from_dict = QuotaIncreaseRequestResp.from_dict(quota_increase_request_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


