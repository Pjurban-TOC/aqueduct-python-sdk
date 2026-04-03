# AuditLogEntryPerformance

Performance metrics. TTFT, TBT per Metron [arXiv:2407.07000]. Prefill vs. decode tracked separately per Sarathi-Serve [OSDI 2024]. Raw latencies (not normalized) per LLM-Inference-Bench [arXiv:2411.00136]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_latency_ms** | **int** | Total request-to-response latency in milliseconds. | [optional] 
**ttft_ms** | **int** | Time To First Token in milliseconds. | [optional] 
**tbt_ms** | **float** | Average Time Between Tokens in milliseconds. | [optional] 
**prefill_latency_ms** | **int** | Prefill phase latency (Sarathi-Serve metric). | [optional] 
**decode_latency_ms** | **int** | Decode phase latency (Sarathi-Serve metric). | [optional] 
**tokens_per_second** | **float** | Token generation throughput. | [optional] 
**queue_time_ms** | **int** | Time spent waiting in the request queue. | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_performance import AuditLogEntryPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryPerformance from a JSON string
audit_log_entry_performance_instance = AuditLogEntryPerformance.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryPerformance.to_json())

# convert the object into a dict
audit_log_entry_performance_dict = audit_log_entry_performance_instance.to_dict()
# create an instance of AuditLogEntryPerformance from a dict
audit_log_entry_performance_from_dict = AuditLogEntryPerformance.from_dict(audit_log_entry_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


