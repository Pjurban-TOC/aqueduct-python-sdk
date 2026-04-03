# AlertThreshold

Alert threshold configuration for a metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_id** | **str** |  | [optional] 
**metric_name** | [**MetricName**](MetricName.md) |  | 
**warning_threshold** | **float** | Value at which a warning alert is triggered. | 
**critical_threshold** | **float** | Value at which a critical alert is triggered. | 
**min_affected_pct** | **float** | Minimum percentage of requests that must be affected. | [optional] 
**enabled** | **bool** |  | 
**tenant_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.alert_threshold import AlertThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of AlertThreshold from a JSON string
alert_threshold_instance = AlertThreshold.from_json(json)
# print the JSON string representation of the object
print(AlertThreshold.to_json())

# convert the object into a dict
alert_threshold_dict = alert_threshold_instance.to_dict()
# create an instance of AlertThreshold from a dict
alert_threshold_from_dict = AlertThreshold.from_dict(alert_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


