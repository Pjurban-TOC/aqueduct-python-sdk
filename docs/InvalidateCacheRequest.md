# InvalidateCacheRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | Glob pattern for cache keys to invalidate. | [optional] 
**keys** | **List[str]** | Specific cache keys to invalidate. | [optional] 
**tags** | **List[str]** | Cache tags to invalidate. | [optional] 

## Example

```python
from aqueduct_sdk.models.invalidate_cache_request import InvalidateCacheRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateCacheRequest from a JSON string
invalidate_cache_request_instance = InvalidateCacheRequest.from_json(json)
# print the JSON string representation of the object
print(InvalidateCacheRequest.to_json())

# convert the object into a dict
invalidate_cache_request_dict = invalidate_cache_request_instance.to_dict()
# create an instance of InvalidateCacheRequest from a dict
invalidate_cache_request_from_dict = InvalidateCacheRequest.from_dict(invalidate_cache_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


