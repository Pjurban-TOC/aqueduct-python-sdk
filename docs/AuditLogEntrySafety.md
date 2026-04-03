# AuditLogEntrySafety

Safety guardrail results for this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scanned** | **bool** |  | [optional] 
**safe** | **bool** |  | [optional] 
**action_taken** | **str** |  | [optional] 
**findings** | [**List[AuditLogEntrySafetyFindingsInner]**](AuditLogEntrySafetyFindingsInner.md) |  | [optional] 
**guardrail_config_id** | **str** |  | [optional] 
**scan_duration_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_safety import AuditLogEntrySafety

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntrySafety from a JSON string
audit_log_entry_safety_instance = AuditLogEntrySafety.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntrySafety.to_json())

# convert the object into a dict
audit_log_entry_safety_dict = audit_log_entry_safety_instance.to_dict()
# create an instance of AuditLogEntrySafety from a dict
audit_log_entry_safety_from_dict = AuditLogEntrySafety.from_dict(audit_log_entry_safety_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


