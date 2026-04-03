# CacheHitStats

Cache hit rate statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_requests** | **int** |  | [optional] 
**cache_hits** | **int** |  | [optional] 
**cache_misses** | **int** |  | [optional] 
**hit_rate** | **float** |  | [optional] 
**hit_rate_by_type** | **Dict[str, float]** |  | [optional] 
**hit_rate_by_pop** | **Dict[str, float]** |  | [optional] 
**sw_cache_hits** | **int** |  | [optional] 
**sw_hit_rate** | **float** |  | [optional] 
**target_hit_rate** | **float** |  | [optional] 
**target_met** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.cache_hit_stats import CacheHitStats

# TODO update the JSON string below
json = "{}"
# create an instance of CacheHitStats from a JSON string
cache_hit_stats_instance = CacheHitStats.from_json(json)
# print the JSON string representation of the object
print(CacheHitStats.to_json())

# convert the object into a dict
cache_hit_stats_dict = cache_hit_stats_instance.to_dict()
# create an instance of CacheHitStats from a dict
cache_hit_stats_from_dict = CacheHitStats.from_dict(cache_hit_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


