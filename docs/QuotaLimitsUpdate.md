# QuotaLimitsUpdate

Quota limit updates. Matches `quotas.go:103` QuotaLimitsUpdate. All fields optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **int** |  | [optional] 
**requests_per_month** | **int** |  | [optional] 
**api_calls_per_hour** | **int** |  | [optional] 
**storage_gb** | **float** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_limits_update import QuotaLimitsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaLimitsUpdate from a JSON string
quota_limits_update_instance = QuotaLimitsUpdate.from_json(json)
# print the JSON string representation of the object
print(QuotaLimitsUpdate.to_json())

# convert the object into a dict
quota_limits_update_dict = quota_limits_update_instance.to_dict()
# create an instance of QuotaLimitsUpdate from a dict
quota_limits_update_from_dict = QuotaLimitsUpdate.from_dict(quota_limits_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


