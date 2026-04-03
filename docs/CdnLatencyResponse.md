# CdnLatencyResponse

CDN latency response with target compliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**CDNLatencyStats**](CDNLatencyStats.md) |  | 
**target_p95_ms** | **float** |  | 
**target_met** | **bool** |  | 
**requirement** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.cdn_latency_response import CdnLatencyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CdnLatencyResponse from a JSON string
cdn_latency_response_instance = CdnLatencyResponse.from_json(json)
# print the JSON string representation of the object
print(CdnLatencyResponse.to_json())

# convert the object into a dict
cdn_latency_response_dict = cdn_latency_response_instance.to_dict()
# create an instance of CdnLatencyResponse from a dict
cdn_latency_response_from_dict = CdnLatencyResponse.from_dict(cdn_latency_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


