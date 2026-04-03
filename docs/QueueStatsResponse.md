# QueueStatsResponse

Aggregate statistics for the breakpoint review queue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant these stats apply to. | 
**total_pending** | **int** | Number of requests currently awaiting review. | 
**by_priority** | **Dict[str, int]** | Pending count broken down by priority level (e.g. low, normal, high, critical). | 
**by_stage** | **Dict[str, int]** | Pending count broken down by pipeline stage. | 
**oldest_pending** | **datetime** | Timestamp of the oldest pending request. Absent when the queue is empty. | [optional] 
**avg_wait_time_seconds** | **float** | Average wait time (in seconds) for requests currently in the queue. | 
**updated_at** | **datetime** | Timestamp when these statistics were computed. | 

## Example

```python
from aqueduct_sdk.models.queue_stats_response import QueueStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueueStatsResponse from a JSON string
queue_stats_response_instance = QueueStatsResponse.from_json(json)
# print the JSON string representation of the object
print(QueueStatsResponse.to_json())

# convert the object into a dict
queue_stats_response_dict = queue_stats_response_instance.to_dict()
# create an instance of QueueStatsResponse from a dict
queue_stats_response_from_dict = QueueStatsResponse.from_dict(queue_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


