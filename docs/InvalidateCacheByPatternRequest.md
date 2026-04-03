# InvalidateCacheByPatternRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | Glob pattern for cache key matching. | 

## Example

```python
from aqueduct_sdk.models.invalidate_cache_by_pattern_request import InvalidateCacheByPatternRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateCacheByPatternRequest from a JSON string
invalidate_cache_by_pattern_request_instance = InvalidateCacheByPatternRequest.from_json(json)
# print the JSON string representation of the object
print(InvalidateCacheByPatternRequest.to_json())

# convert the object into a dict
invalidate_cache_by_pattern_request_dict = invalidate_cache_by_pattern_request_instance.to_dict()
# create an instance of InvalidateCacheByPatternRequest from a dict
invalidate_cache_by_pattern_request_from_dict = InvalidateCacheByPatternRequest.from_dict(invalidate_cache_by_pattern_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


