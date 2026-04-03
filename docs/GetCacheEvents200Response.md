# GetCacheEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[GetCacheEvents200ResponseEventsInner]**](GetCacheEvents200ResponseEventsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_cache_events200_response import GetCacheEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCacheEvents200Response from a JSON string
get_cache_events200_response_instance = GetCacheEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetCacheEvents200Response.to_json())

# convert the object into a dict
get_cache_events200_response_dict = get_cache_events200_response_instance.to_dict()
# create an instance of GetCacheEvents200Response from a dict
get_cache_events200_response_from_dict = GetCacheEvents200Response.from_dict(get_cache_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


