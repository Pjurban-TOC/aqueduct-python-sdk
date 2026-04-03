# QuotaIncreaseRequestReq

Self-service quota increase request. Matches `quotas.go:132` QuotaIncreaseRequestReq.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Resource to increase. | 
**requested_limit** | **int** | Desired new limit value. | 
**justification** | **str** | Business justification (minimum 20 characters). | 
**urgency** | **str** | Request urgency level. | [optional] [default to 'normal']

## Example

```python
from aqueduct_sdk.models.quota_increase_request_req import QuotaIncreaseRequestReq

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaIncreaseRequestReq from a JSON string
quota_increase_request_req_instance = QuotaIncreaseRequestReq.from_json(json)
# print the JSON string representation of the object
print(QuotaIncreaseRequestReq.to_json())

# convert the object into a dict
quota_increase_request_req_dict = quota_increase_request_req_instance.to_dict()
# create an instance of QuotaIncreaseRequestReq from a dict
quota_increase_request_req_from_dict = QuotaIncreaseRequestReq.from_dict(quota_increase_request_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


