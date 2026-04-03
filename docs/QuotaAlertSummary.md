# QuotaAlertSummary

Brief alert info in quota status. Matches `quotas.go:88` QuotaAlertSummary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** |  | 
**threshold** | **str** | Threshold that was crossed (e.g., \&quot;80%\&quot;, \&quot;soft_limit\&quot;). | 
**triggered_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.quota_alert_summary import QuotaAlertSummary

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaAlertSummary from a JSON string
quota_alert_summary_instance = QuotaAlertSummary.from_json(json)
# print the JSON string representation of the object
print(QuotaAlertSummary.to_json())

# convert the object into a dict
quota_alert_summary_dict = quota_alert_summary_instance.to_dict()
# create an instance of QuotaAlertSummary from a dict
quota_alert_summary_from_dict = QuotaAlertSummary.from_dict(quota_alert_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


