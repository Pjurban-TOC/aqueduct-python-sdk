# Anomaly

Detected anomaly. Matches domain/anomaly.go Anomaly struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_id** | **str** | Anomaly identifier (format &#x60;anom_{random12}&#x60;). | 
**tenant_id** | **str** |  | 
**metric_name** | **str** |  | 
**current_value** | **float** |  | 
**baseline_value** | **float** |  | 
**baseline_mean** | **float** |  | [optional] 
**baseline_stddev** | **float** |  | [optional] 
**z_score** | **float** |  | [optional] 
**deviation_sigma** | **float** |  | [optional] 
**deviation_pct** | **float** |  | [optional] 
**direction** | **str** |  | [optional] 
**detected_at** | **datetime** |  | 
**sustained_from** | **datetime** |  | 
**resolved_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**severity** | **str** |  | 
**alerted_at** | **datetime** |  | [optional] 
**alert_count** | **int** |  | [optional] 
**acknowledged** | **bool** |  | [optional] 
**acknowledged_by** | **str** |  | [optional] 
**acknowledged_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.anomaly import Anomaly

# TODO update the JSON string below
json = "{}"
# create an instance of Anomaly from a JSON string
anomaly_instance = Anomaly.from_json(json)
# print the JSON string representation of the object
print(Anomaly.to_json())

# convert the object into a dict
anomaly_dict = anomaly_instance.to_dict()
# create an instance of Anomaly from a dict
anomaly_from_dict = Anomaly.from_dict(anomaly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


