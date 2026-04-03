# AuditLogEntryComplianceViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_compliance_violations_inner import AuditLogEntryComplianceViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryComplianceViolationsInner from a JSON string
audit_log_entry_compliance_violations_inner_instance = AuditLogEntryComplianceViolationsInner.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryComplianceViolationsInner.to_json())

# convert the object into a dict
audit_log_entry_compliance_violations_inner_dict = audit_log_entry_compliance_violations_inner_instance.to_dict()
# create an instance of AuditLogEntryComplianceViolationsInner from a dict
audit_log_entry_compliance_violations_inner_from_dict = AuditLogEntryComplianceViolationsInner.from_dict(audit_log_entry_compliance_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


