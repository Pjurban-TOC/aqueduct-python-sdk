# AcknowledgePerformanceAlert200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**alert_id** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.acknowledge_performance_alert200_response import AcknowledgePerformanceAlert200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgePerformanceAlert200Response from a JSON string
acknowledge_performance_alert200_response_instance = AcknowledgePerformanceAlert200Response.from_json(json)
# print the JSON string representation of the object
print(AcknowledgePerformanceAlert200Response.to_json())

# convert the object into a dict
acknowledge_performance_alert200_response_dict = acknowledge_performance_alert200_response_instance.to_dict()
# create an instance of AcknowledgePerformanceAlert200Response from a dict
acknowledge_performance_alert200_response_from_dict = AcknowledgePerformanceAlert200Response.from_dict(acknowledge_performance_alert200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


