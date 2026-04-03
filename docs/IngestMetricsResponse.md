# IngestMetricsResponse

Response for metric ingestion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**metrics_recorded** | **int** |  | 
**alerts** | [**List[PerformanceAlert]**](PerformanceAlert.md) | Any alerts triggered by the ingested metrics. | [optional] 
**processing_ms** | **int** |  | 

## Example

```python
from aqueduct_sdk.models.ingest_metrics_response import IngestMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IngestMetricsResponse from a JSON string
ingest_metrics_response_instance = IngestMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(IngestMetricsResponse.to_json())

# convert the object into a dict
ingest_metrics_response_dict = ingest_metrics_response_instance.to_dict()
# create an instance of IngestMetricsResponse from a dict
ingest_metrics_response_from_dict = IngestMetricsResponse.from_dict(ingest_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


