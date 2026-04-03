# AuditLogEntrySafetyFindingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_type** | **str** |  | [optional] 
**detected** | **bool** |  | [optional] 
**score** | **float** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_safety_findings_inner import AuditLogEntrySafetyFindingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntrySafetyFindingsInner from a JSON string
audit_log_entry_safety_findings_inner_instance = AuditLogEntrySafetyFindingsInner.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntrySafetyFindingsInner.to_json())

# convert the object into a dict
audit_log_entry_safety_findings_inner_dict = audit_log_entry_safety_findings_inner_instance.to_dict()
# create an instance of AuditLogEntrySafetyFindingsInner from a dict
audit_log_entry_safety_findings_inner_from_dict = AuditLogEntrySafetyFindingsInner.from_dict(audit_log_entry_safety_findings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


