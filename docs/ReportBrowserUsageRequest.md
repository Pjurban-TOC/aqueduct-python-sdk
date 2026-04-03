# ReportBrowserUsageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**features_used** | **List[str]** |  | [optional] 
**page_views** | **int** |  | [optional] 
**duration_seconds** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.report_browser_usage_request import ReportBrowserUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReportBrowserUsageRequest from a JSON string
report_browser_usage_request_instance = ReportBrowserUsageRequest.from_json(json)
# print the JSON string representation of the object
print(ReportBrowserUsageRequest.to_json())

# convert the object into a dict
report_browser_usage_request_dict = report_browser_usage_request_instance.to_dict()
# create an instance of ReportBrowserUsageRequest from a dict
report_browser_usage_request_from_dict = ReportBrowserUsageRequest.from_dict(report_browser_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


