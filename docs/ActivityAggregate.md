# ActivityAggregate

Activity aggregate. Matches domain/event.go ActivityAggregate struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**window_type** | **str** |  | 
**window_start** | **datetime** |  | 
**window_end** | **datetime** |  | 
**event_count** | **int** |  | 
**unique_users** | **int** |  | [optional] 
**error_count** | **int** |  | [optional] 
**error_rate** | **float** |  | [optional] 
**action_distribution** | **Dict[str, int]** |  | [optional] 
**resource_distribution** | **Dict[str, int]** |  | [optional] 
**outcome_distribution** | **Dict[str, int]** |  | [optional] 
**top_users** | [**List[ActivityAggregateTopUsersInner]**](ActivityAggregateTopUsersInner.md) |  | [optional] 
**top_resources** | [**List[ActivityAggregateTopResourcesInner]**](ActivityAggregateTopResourcesInner.md) |  | [optional] 
**top_actions** | [**List[ActivityAggregateTopActionsInner]**](ActivityAggregateTopActionsInner.md) |  | [optional] 
**computed_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.activity_aggregate import ActivityAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAggregate from a JSON string
activity_aggregate_instance = ActivityAggregate.from_json(json)
# print the JSON string representation of the object
print(ActivityAggregate.to_json())

# convert the object into a dict
activity_aggregate_dict = activity_aggregate_instance.to_dict()
# create an instance of ActivityAggregate from a dict
activity_aggregate_from_dict = ActivityAggregate.from_dict(activity_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


