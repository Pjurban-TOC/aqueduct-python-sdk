# ActivityAggregateTopActionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.activity_aggregate_top_actions_inner import ActivityAggregateTopActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAggregateTopActionsInner from a JSON string
activity_aggregate_top_actions_inner_instance = ActivityAggregateTopActionsInner.from_json(json)
# print the JSON string representation of the object
print(ActivityAggregateTopActionsInner.to_json())

# convert the object into a dict
activity_aggregate_top_actions_inner_dict = activity_aggregate_top_actions_inner_instance.to_dict()
# create an instance of ActivityAggregateTopActionsInner from a dict
activity_aggregate_top_actions_inner_from_dict = ActivityAggregateTopActionsInner.from_dict(activity_aggregate_top_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


