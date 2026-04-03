# GetAuditStats200ResponseTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_requests** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**total_cost_usd** | **float** |  | [optional] 
**error_rate** | **float** |  | [optional] 
**avg_latency_ms** | **float** |  | [optional] 
**p50_latency_ms** | **int** |  | [optional] 
**p95_latency_ms** | **int** |  | [optional] 
**p99_latency_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_audit_stats200_response_totals import GetAuditStats200ResponseTotals

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditStats200ResponseTotals from a JSON string
get_audit_stats200_response_totals_instance = GetAuditStats200ResponseTotals.from_json(json)
# print the JSON string representation of the object
print(GetAuditStats200ResponseTotals.to_json())

# convert the object into a dict
get_audit_stats200_response_totals_dict = get_audit_stats200_response_totals_instance.to_dict()
# create an instance of GetAuditStats200ResponseTotals from a dict
get_audit_stats200_response_totals_from_dict = GetAuditStats200ResponseTotals.from_dict(get_audit_stats200_response_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


