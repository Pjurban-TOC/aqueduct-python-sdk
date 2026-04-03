# WebVitalMetricSummary

Summary statistics for a single Web Vital metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | [**MetricName**](MetricName.md) |  | 
**p50** | **float** |  | [optional] 
**p75** | **float** |  | 
**p95** | **float** |  | [optional] 
**p99** | **float** |  | [optional] 
**rating** | **str** | Rating based on Core Web Vitals thresholds. | 
**sample_count** | **int** |  | 
**target_value** | **float** |  | [optional] 
**target_met** | **bool** |  | [optional] 
**unit** | **str** |  | [optional] 
**trend_percent** | **float** | Percentage change from previous period (negative &#x3D; improvement). | [optional] 

## Example

```python
from aqueduct_sdk.models.web_vital_metric_summary import WebVitalMetricSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WebVitalMetricSummary from a JSON string
web_vital_metric_summary_instance = WebVitalMetricSummary.from_json(json)
# print the JSON string representation of the object
print(WebVitalMetricSummary.to_json())

# convert the object into a dict
web_vital_metric_summary_dict = web_vital_metric_summary_instance.to_dict()
# create an instance of WebVitalMetricSummary from a dict
web_vital_metric_summary_from_dict = WebVitalMetricSummary.from_dict(web_vital_metric_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


