# WebVitalsReport

Comprehensive Web Vitals report (AC-UI-045-020).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fcp** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**lcp** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**fid** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**cls** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**ttfb** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**inp** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**tti** | [**WebVitalMetricSummary**](WebVitalMetricSummary.md) |  | [optional] 
**overall_rating** | **str** | Overall rating (good, needs-improvement, poor). | 
**total_samples** | **int** |  | 
**cache_hit_rate** | **float** |  | [optional] 
**cache_target_met** | **bool** |  | [optional] 
**cdn_latency_p95** | **float** |  | [optional] 
**cdn_target_met** | **bool** |  | [optional] 
**active_alerts_count** | **int** |  | [optional] 
**generated_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.web_vitals_report import WebVitalsReport

# TODO update the JSON string below
json = "{}"
# create an instance of WebVitalsReport from a JSON string
web_vitals_report_instance = WebVitalsReport.from_json(json)
# print the JSON string representation of the object
print(WebVitalsReport.to_json())

# convert the object into a dict
web_vitals_report_dict = web_vitals_report_instance.to_dict()
# create an instance of WebVitalsReport from a dict
web_vitals_report_from_dict = WebVitalsReport.from_dict(web_vitals_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


