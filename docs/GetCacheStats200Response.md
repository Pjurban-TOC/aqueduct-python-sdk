# GetCacheStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_keys** | **int** |  | [optional] 
**memory_used_bytes** | **int** |  | [optional] 
**hit_rate** | **float** |  | [optional] 
**evictions** | **int** |  | [optional] 
**invalidations_total** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_cache_stats200_response import GetCacheStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCacheStats200Response from a JSON string
get_cache_stats200_response_instance = GetCacheStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetCacheStats200Response.to_json())

# convert the object into a dict
get_cache_stats200_response_dict = get_cache_stats200_response_instance.to_dict()
# create an instance of GetCacheStats200Response from a dict
get_cache_stats200_response_from_dict = GetCacheStats200Response.from_dict(get_cache_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


