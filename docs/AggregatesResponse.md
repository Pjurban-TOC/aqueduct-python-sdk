# AggregatesResponse

Aggregates response. Matches handler/dashboard.go AggregatesResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregates** | [**List[ActivityAggregate]**](ActivityAggregate.md) |  | 
**time_range** | [**TimeRange**](TimeRange.md) |  | 
**window_type** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from aqueduct_sdk.models.aggregates_response import AggregatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatesResponse from a JSON string
aggregates_response_instance = AggregatesResponse.from_json(json)
# print the JSON string representation of the object
print(AggregatesResponse.to_json())

# convert the object into a dict
aggregates_response_dict = aggregates_response_instance.to_dict()
# create an instance of AggregatesResponse from a dict
aggregates_response_from_dict = AggregatesResponse.from_dict(aggregates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


