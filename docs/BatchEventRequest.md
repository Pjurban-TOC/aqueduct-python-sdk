# BatchEventRequest

Batch event creation request. Matches handler/events.go BatchEventRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ActivityEvent]**](ActivityEvent.md) |  | 

## Example

```python
from aqueduct_sdk.models.batch_event_request import BatchEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEventRequest from a JSON string
batch_event_request_instance = BatchEventRequest.from_json(json)
# print the JSON string representation of the object
print(BatchEventRequest.to_json())

# convert the object into a dict
batch_event_request_dict = batch_event_request_instance.to_dict()
# create an instance of BatchEventRequest from a dict
batch_event_request_from_dict = BatchEventRequest.from_dict(batch_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


