# AuditLogEntryModel

Model information for AI inference requests. Per TRiSM [arXiv:2506.04133], model lineage tracking is required. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | **str** | Requested model identifier. | [optional] 
**model_resolved** | **str** | Actual model used after routing. | [optional] 
**provider** | **str** |  | [optional] 
**model_version** | **str** |  | [optional] 
**routing_policy** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_model import AuditLogEntryModel

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryModel from a JSON string
audit_log_entry_model_instance = AuditLogEntryModel.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryModel.to_json())

# convert the object into a dict
audit_log_entry_model_dict = audit_log_entry_model_instance.to_dict()
# create an instance of AuditLogEntryModel from a dict
audit_log_entry_model_from_dict = AuditLogEntryModel.from_dict(audit_log_entry_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


