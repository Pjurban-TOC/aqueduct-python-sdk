# QuotaLimit

Single quota limit with usage. Matches `quotas.go:79` QuotaLimit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max** | **int** | Hard limit value. | 
**current** | **int** | Current usage count. | 
**soft_limit** | **int** | Soft limit threshold that triggers alerts. | 
**percent_used** | **float** | Current usage as a percentage of the hard limit. | 
**reset_date** | **datetime** | When the quota counter resets. | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_limit import QuotaLimit

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaLimit from a JSON string
quota_limit_instance = QuotaLimit.from_json(json)
# print the JSON string representation of the object
print(QuotaLimit.to_json())

# convert the object into a dict
quota_limit_dict = quota_limit_instance.to_dict()
# create an instance of QuotaLimit from a dict
quota_limit_from_dict = QuotaLimit.from_dict(quota_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


