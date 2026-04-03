# ActivityAggregateTopResourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.activity_aggregate_top_resources_inner import ActivityAggregateTopResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityAggregateTopResourcesInner from a JSON string
activity_aggregate_top_resources_inner_instance = ActivityAggregateTopResourcesInner.from_json(json)
# print the JSON string representation of the object
print(ActivityAggregateTopResourcesInner.to_json())

# convert the object into a dict
activity_aggregate_top_resources_inner_dict = activity_aggregate_top_resources_inner_instance.to_dict()
# create an instance of ActivityAggregateTopResourcesInner from a dict
activity_aggregate_top_resources_inner_from_dict = ActivityAggregateTopResourcesInner.from_dict(activity_aggregate_top_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


