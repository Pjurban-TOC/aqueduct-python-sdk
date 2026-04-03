# CacheHitRateResponse

Cache hit rate response with target compliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**CacheHitStats**](CacheHitStats.md) |  | 
**target_hit_rate** | **float** |  | 
**target_met** | **bool** |  | 
**requirement** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.cache_hit_rate_response import CacheHitRateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CacheHitRateResponse from a JSON string
cache_hit_rate_response_instance = CacheHitRateResponse.from_json(json)
# print the JSON string representation of the object
print(CacheHitRateResponse.to_json())

# convert the object into a dict
cache_hit_rate_response_dict = cache_hit_rate_response_instance.to_dict()
# create an instance of CacheHitRateResponse from a dict
cache_hit_rate_response_from_dict = CacheHitRateResponse.from_dict(cache_hit_rate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


