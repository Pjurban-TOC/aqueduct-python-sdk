# DashboardSummary

Dashboard summary. Matches aggregation/service.go DashboardSummary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**total_events** | **int** |  | 
**unique_users** | **int** |  | 
**total_errors** | **int** |  | 
**error_rate** | **float** |  | 
**action_breakdown** | **Dict[str, int]** |  | [optional] 
**aggregates** | [**List[ActivityAggregate]**](ActivityAggregate.md) |  | [optional] 
**generated_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.dashboard_summary import DashboardSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardSummary from a JSON string
dashboard_summary_instance = DashboardSummary.from_json(json)
# print the JSON string representation of the object
print(DashboardSummary.to_json())

# convert the object into a dict
dashboard_summary_dict = dashboard_summary_instance.to_dict()
# create an instance of DashboardSummary from a dict
dashboard_summary_from_dict = DashboardSummary.from_dict(dashboard_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


