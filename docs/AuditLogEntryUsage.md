# AuditLogEntryUsage

Token usage and cost tracking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | [optional] 
**completion_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**estimated_cost_usd** | **float** | Estimated cost in USD based on provider pricing. | [optional] 
**cached_tokens** | **int** | Tokens served from cache (not billed). | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_usage import AuditLogEntryUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryUsage from a JSON string
audit_log_entry_usage_instance = AuditLogEntryUsage.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryUsage.to_json())

# convert the object into a dict
audit_log_entry_usage_dict = audit_log_entry_usage_instance.to_dict()
# create an instance of AuditLogEntryUsage from a dict
audit_log_entry_usage_from_dict = AuditLogEntryUsage.from_dict(audit_log_entry_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


