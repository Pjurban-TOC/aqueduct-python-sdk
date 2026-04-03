# AuditLogEntryDlp

DLP scan results for this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scanned** | **bool** |  | [optional] 
**findings_count** | **int** |  | [optional] 
**blocked** | **bool** |  | [optional] 
**policy_id** | **str** |  | [optional] 
**scan_duration_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_dlp import AuditLogEntryDlp

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryDlp from a JSON string
audit_log_entry_dlp_instance = AuditLogEntryDlp.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryDlp.to_json())

# convert the object into a dict
audit_log_entry_dlp_dict = audit_log_entry_dlp_instance.to_dict()
# create an instance of AuditLogEntryDlp from a dict
audit_log_entry_dlp_from_dict = AuditLogEntryDlp.from_dict(audit_log_entry_dlp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


