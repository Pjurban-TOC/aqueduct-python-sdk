# PerformanceAlert

Performance threshold alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id** | **str** |  | 
**threshold_id** | **str** |  | [optional] 
**metric_name** | [**MetricName**](MetricName.md) |  | 
**severity** | **str** |  | 
**status** | **str** |  | 
**threshold_value** | **float** |  | 
**actual_value** | **float** |  | 
**affected_pct** | **float** | Percentage of requests affected. | [optional] 
**message** | **str** |  | 
**tenant_id** | **str** |  | 
**triggered_at** | **datetime** |  | 
**acknowledged_at** | **datetime** |  | [optional] 
**acknowledged_by** | **str** |  | [optional] 
**resolved_at** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.performance_alert import PerformanceAlert

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceAlert from a JSON string
performance_alert_instance = PerformanceAlert.from_json(json)
# print the JSON string representation of the object
print(PerformanceAlert.to_json())

# convert the object into a dict
performance_alert_dict = performance_alert_instance.to_dict()
# create an instance of PerformanceAlert from a dict
performance_alert_from_dict = PerformanceAlert.from_dict(performance_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


