# QuotaAlertDetail

Quota alert detail. Matches `quotas.go:153` QuotaAlertDetail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** |  | 
**resource** | **str** |  | 
**threshold** | **str** |  | 
**current_value** | **int** |  | 
**limit_value** | **int** |  | 
**triggered_at** | **datetime** |  | 
**acknowledged** | **bool** |  | 
**acknowledged_by** | **str** |  | [optional] 
**acknowledged_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_alert_detail import QuotaAlertDetail

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaAlertDetail from a JSON string
quota_alert_detail_instance = QuotaAlertDetail.from_json(json)
# print the JSON string representation of the object
print(QuotaAlertDetail.to_json())

# convert the object into a dict
quota_alert_detail_dict = quota_alert_detail_instance.to_dict()
# create an instance of QuotaAlertDetail from a dict
quota_alert_detail_from_dict = QuotaAlertDetail.from_dict(quota_alert_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


