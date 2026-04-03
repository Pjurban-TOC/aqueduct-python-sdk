# AssetTimeSeries

Time series data for an asset metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_type** | **str** |  | 
**data_points** | [**List[AssetTimeSeriesDataPoint]**](AssetTimeSeriesDataPoint.md) |  | 
**unit** | **str** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.asset_time_series import AssetTimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTimeSeries from a JSON string
asset_time_series_instance = AssetTimeSeries.from_json(json)
# print the JSON string representation of the object
print(AssetTimeSeries.to_json())

# convert the object into a dict
asset_time_series_dict = asset_time_series_instance.to_dict()
# create an instance of AssetTimeSeries from a dict
asset_time_series_from_dict = AssetTimeSeries.from_dict(asset_time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


