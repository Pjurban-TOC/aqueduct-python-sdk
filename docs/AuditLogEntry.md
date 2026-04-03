# AuditLogEntry

Comprehensive audit log entry following the Kong AI Gateway audit reference. Every API call is logged with full request/response metadata per AEGIS [arXiv:2603.12621]. Supports per-request compliance evaluation via policy-as-code per ISpec [arXiv:2512.17259]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique audit event identifier (ULID). | 
**trace_id** | **str** | Distributed trace ID for request correlation. | [optional] 
**request_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**api_key_id** | **str** | API key used (if applicable, not the key itself). | [optional] 
**session_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | 
**request** | [**AuditLogEntryRequest**](AuditLogEntryRequest.md) |  | 
**response** | [**AuditLogEntryResponse**](AuditLogEntryResponse.md) |  | [optional] 
**model** | [**AuditLogEntryModel**](AuditLogEntryModel.md) |  | [optional] 
**usage** | [**AuditLogEntryUsage**](AuditLogEntryUsage.md) |  | [optional] 
**performance** | [**AuditLogEntryPerformance**](AuditLogEntryPerformance.md) |  | [optional] 
**dlp** | [**AuditLogEntryDlp**](AuditLogEntryDlp.md) |  | [optional] 
**safety** | [**AuditLogEntrySafety**](AuditLogEntrySafety.md) |  | [optional] 
**rag** | [**AuditLogEntryRag**](AuditLogEntryRag.md) |  | [optional] 
**cache** | [**AuditLogEntryCache**](AuditLogEntryCache.md) |  | [optional] 
**compliance** | [**AuditLogEntryCompliance**](AuditLogEntryCompliance.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry import AuditLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntry from a JSON string
audit_log_entry_instance = AuditLogEntry.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntry.to_json())

# convert the object into a dict
audit_log_entry_dict = audit_log_entry_instance.to_dict()
# create an instance of AuditLogEntry from a dict
audit_log_entry_from_dict = AuditLogEntry.from_dict(audit_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


