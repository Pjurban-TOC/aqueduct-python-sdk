# BatchEventResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**event_id** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.batch_event_response_errors_inner import BatchEventResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEventResponseErrorsInner from a JSON string
batch_event_response_errors_inner_instance = BatchEventResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(BatchEventResponseErrorsInner.to_json())

# convert the object into a dict
batch_event_response_errors_inner_dict = batch_event_response_errors_inner_instance.to_dict()
# create an instance of BatchEventResponseErrorsInner from a dict
batch_event_response_errors_inner_from_dict = BatchEventResponseErrorsInner.from_dict(batch_event_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


