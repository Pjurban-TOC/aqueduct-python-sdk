# AssetMetricBatch

Batch of frontend asset performance metrics for ingestion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**page_url** | **str** |  | [optional] 
**metrics** | [**List[AssetMetric]**](AssetMetric.md) |  | 
**timestamp** | **datetime** |  | 
**connection_type** | **str** |  | [optional] 
**downlink_mbps** | **float** |  | [optional] 
**rtt_ms** | **float** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.asset_metric_batch import AssetMetricBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetricBatch from a JSON string
asset_metric_batch_instance = AssetMetricBatch.from_json(json)
# print the JSON string representation of the object
print(AssetMetricBatch.to_json())

# convert the object into a dict
asset_metric_batch_dict = asset_metric_batch_instance.to_dict()
# create an instance of AssetMetricBatch from a dict
asset_metric_batch_from_dict = AssetMetricBatch.from_dict(asset_metric_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


