# TenantDashboardResponse

Tenant-specific dashboard. Matches handler/dashboard.go TenantDashboardResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**summary** | [**DashboardSummary**](DashboardSummary.md) |  | 
**active_anomalies** | **int** |  | 
**anomalies** | [**List[Anomaly]**](Anomaly.md) |  | [optional] 
**time_range** | [**TimeRange**](TimeRange.md) |  | 

## Example

```python
from aqueduct_sdk.models.tenant_dashboard_response import TenantDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDashboardResponse from a JSON string
tenant_dashboard_response_instance = TenantDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(TenantDashboardResponse.to_json())

# convert the object into a dict
tenant_dashboard_response_dict = tenant_dashboard_response_instance.to_dict()
# create an instance of TenantDashboardResponse from a dict
tenant_dashboard_response_from_dict = TenantDashboardResponse.from_dict(tenant_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


