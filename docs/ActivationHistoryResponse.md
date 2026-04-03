# ActivationHistoryResponse

Activation history for a breakpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**history** | [**List[ActivationRecordResponse]**](ActivationRecordResponse.md) |  | 

## Example

```python
from aqueduct_sdk.models.activation_history_response import ActivationHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationHistoryResponse from a JSON string
activation_history_response_instance = ActivationHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(ActivationHistoryResponse.to_json())

# convert the object into a dict
activation_history_response_dict = activation_history_response_instance.to_dict()
# create an instance of ActivationHistoryResponse from a dict
activation_history_response_from_dict = ActivationHistoryResponse.from_dict(activation_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


