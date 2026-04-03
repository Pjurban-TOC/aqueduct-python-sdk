# AuditLogQueryResponseAggregations

Optional aggregated statistics for the query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_requests** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**total_cost_usd** | **float** |  | [optional] 
**avg_latency_ms** | **float** |  | [optional] 
**error_rate** | **float** |  | [optional] 
**p50_latency_ms** | **int** |  | [optional] 
**p95_latency_ms** | **int** |  | [optional] 
**p99_latency_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_query_response_aggregations import AuditLogQueryResponseAggregations

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogQueryResponseAggregations from a JSON string
audit_log_query_response_aggregations_instance = AuditLogQueryResponseAggregations.from_json(json)
# print the JSON string representation of the object
print(AuditLogQueryResponseAggregations.to_json())

# convert the object into a dict
audit_log_query_response_aggregations_dict = audit_log_query_response_aggregations_instance.to_dict()
# create an instance of AuditLogQueryResponseAggregations from a dict
audit_log_query_response_aggregations_from_dict = AuditLogQueryResponseAggregations.from_dict(audit_log_query_response_aggregations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


