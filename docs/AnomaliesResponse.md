# AnomaliesResponse

Anomalies list response. Matches handler/dashboard.go AnomaliesResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalies** | [**List[Anomaly]**](Anomaly.md) |  | 
**count** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.anomalies_response import AnomaliesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnomaliesResponse from a JSON string
anomalies_response_instance = AnomaliesResponse.from_json(json)
# print the JSON string representation of the object
print(AnomaliesResponse.to_json())

# convert the object into a dict
anomalies_response_dict = anomalies_response_instance.to_dict()
# create an instance of AnomaliesResponse from a dict
anomalies_response_from_dict = AnomaliesResponse.from_dict(anomalies_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


