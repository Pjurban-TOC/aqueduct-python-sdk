# GetCacheEvents200ResponseEventsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | [optional] 
**pattern** | **str** |  | [optional] 
**keys_affected** | **int** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_cache_events200_response_events_inner import GetCacheEvents200ResponseEventsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCacheEvents200ResponseEventsInner from a JSON string
get_cache_events200_response_events_inner_instance = GetCacheEvents200ResponseEventsInner.from_json(json)
# print the JSON string representation of the object
print(GetCacheEvents200ResponseEventsInner.to_json())

# convert the object into a dict
get_cache_events200_response_events_inner_dict = get_cache_events200_response_events_inner_instance.to_dict()
# create an instance of GetCacheEvents200ResponseEventsInner from a dict
get_cache_events200_response_events_inner_from_dict = GetCacheEvents200ResponseEventsInner.from_dict(get_cache_events200_response_events_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


