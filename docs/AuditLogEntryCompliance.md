# AuditLogEntryCompliance

Per-request compliance evaluation per ISpec [arXiv:2512.17259]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies_evaluated** | **List[str]** |  | [optional] 
**violations** | [**List[AuditLogEntryComplianceViolationsInner]**](AuditLogEntryComplianceViolationsInner.md) |  | [optional] 
**compliant** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_compliance import AuditLogEntryCompliance

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryCompliance from a JSON string
audit_log_entry_compliance_instance = AuditLogEntryCompliance.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryCompliance.to_json())

# convert the object into a dict
audit_log_entry_compliance_dict = audit_log_entry_compliance_instance.to_dict()
# create an instance of AuditLogEntryCompliance from a dict
audit_log_entry_compliance_from_dict = AuditLogEntryCompliance.from_dict(audit_log_entry_compliance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


