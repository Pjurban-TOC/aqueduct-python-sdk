# ActivityAggregateTopUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.activity_aggregate_top_users_inner import ActivityAggregateTopUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAggregateTopUsersInner from a JSON string
activity_aggregate_top_users_inner_instance = ActivityAggregateTopUsersInner.from_json(json)
# print the JSON string representation of the object
print(ActivityAggregateTopUsersInner.to_json())

# convert the object into a dict
activity_aggregate_top_users_inner_dict = activity_aggregate_top_users_inner_instance.to_dict()
# create an instance of ActivityAggregateTopUsersInner from a dict
activity_aggregate_top_users_inner_from_dict = ActivityAggregateTopUsersInner.from_dict(activity_aggregate_top_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


