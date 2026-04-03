# BatchEventResponse

Batch event creation response. Matches handler/events.go BatchEventResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_received** | **int** |  | 
**total_accepted** | **int** |  | 
**total_rejected** | **int** |  | 
**errors** | [**List[BatchEventResponseErrorsInner]**](BatchEventResponseErrorsInner.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.batch_event_response import BatchEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEventResponse from a JSON string
batch_event_response_instance = BatchEventResponse.from_json(json)
# print the JSON string representation of the object
print(BatchEventResponse.to_json())

# convert the object into a dict
batch_event_response_dict = batch_event_response_instance.to_dict()
# create an instance of BatchEventResponse from a dict
batch_event_response_from_dict = BatchEventResponse.from_dict(batch_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


