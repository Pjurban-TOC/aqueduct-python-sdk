# AssetMetric

Individual asset performance metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**asset_url** | **str** |  | 
**type** | **str** | Asset type. | 
**size_bytes** | **int** |  | [optional] 
**transfer_bytes** | **int** |  | [optional] 
**load_time_ms** | **float** |  | 
**dns_time_ms** | **float** |  | [optional] 
**connect_time_ms** | **float** |  | [optional] 
**tls_time_ms** | **float** |  | [optional] 
**ttfb_ms** | **float** |  | [optional] 
**download_time_ms** | **float** |  | [optional] 
**cache_hit** | **bool** |  | [optional] 
**cdn_pop** | **str** | CDN point of presence that served this asset. | [optional] 
**encoding** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**initiator_type** | **str** |  | [optional] 
**service_worker_used** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.asset_metric import AssetMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetric from a JSON string
asset_metric_instance = AssetMetric.from_json(json)
# print the JSON string representation of the object
print(AssetMetric.to_json())

# convert the object into a dict
asset_metric_dict = asset_metric_instance.to_dict()
# create an instance of AssetMetric from a dict
asset_metric_from_dict = AssetMetric.from_dict(asset_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


