# CDNLatencyStats

CDN latency percentile statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p50_ms** | **float** |  | [optional] 
**p75_ms** | **float** |  | [optional] 
**p90_ms** | **float** |  | [optional] 
**p95_ms** | **float** |  | [optional] 
**p99_ms** | **float** |  | [optional] 
**sample_count** | **int** |  | [optional] 
**p95_by_pop** | **Dict[str, float]** |  | [optional] 
**p95_by_type** | **Dict[str, float]** |  | [optional] 
**target_p95_ms** | **float** |  | [optional] 
**target_met** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.cdn_latency_stats import CDNLatencyStats

# TODO update the JSON string below
json = "{}"
# create an instance of CDNLatencyStats from a JSON string
cdn_latency_stats_instance = CDNLatencyStats.from_json(json)
# print the JSON string representation of the object
print(CDNLatencyStats.to_json())

# convert the object into a dict
cdn_latency_stats_dict = cdn_latency_stats_instance.to_dict()
# create an instance of CDNLatencyStats from a dict
cdn_latency_stats_from_dict = CDNLatencyStats.from_dict(cdn_latency_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


