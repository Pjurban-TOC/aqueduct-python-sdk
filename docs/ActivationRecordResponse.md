# ActivationRecordResponse

A single activation (trigger) record for a breakpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**breakpoint_id** | **str** |  | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | 
**correlation_id** | **str** |  | 
**stage** | **str** |  | 
**mode** | **str** |  | 
**decision** | **str** | Outcome of the activation (e.g. approved, rejected, expired). | 
**reviewed_by** | **str** | User who reviewed the activation (if applicable). | [optional] 
**reviewed_at** | **datetime** | Timestamp of the review. Absent if not yet reviewed. | [optional] 
**activated_at** | **datetime** | Timestamp when the breakpoint was triggered. | 

## Example

```python
from aqueduct_sdk.models.activation_record_response import ActivationRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivationRecordResponse from a JSON string
activation_record_response_instance = ActivationRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ActivationRecordResponse.to_json())

# convert the object into a dict
activation_record_response_dict = activation_record_response_instance.to_dict()
# create an instance of ActivationRecordResponse from a dict
activation_record_response_from_dict = ActivationRecordResponse.from_dict(activation_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


