# AssetTimeSeriesDataPoint

Single time series data point with percentiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**value** | **float** |  | 
**p50** | **float** |  | [optional] 
**p95** | **float** |  | [optional] 
**p99** | **float** |  | [optional] 
**sample_count** | **int** |  | 

## Example

```python
from aqueduct_sdk.models.asset_time_series_data_point import AssetTimeSeriesDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTimeSeriesDataPoint from a JSON string
asset_time_series_data_point_instance = AssetTimeSeriesDataPoint.from_json(json)
# print the JSON string representation of the object
print(AssetTimeSeriesDataPoint.to_json())

# convert the object into a dict
asset_time_series_data_point_dict = asset_time_series_data_point_instance.to_dict()
# create an instance of AssetTimeSeriesDataPoint from a dict
asset_time_series_data_point_from_dict = AssetTimeSeriesDataPoint.from_dict(asset_time_series_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


