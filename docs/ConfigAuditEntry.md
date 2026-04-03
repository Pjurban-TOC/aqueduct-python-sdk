# ConfigAuditEntry

An audit log entry for configuration changes. Matches `config.go` ConfigAuditEntry struct. The `tenant_id` field is omitted for global configuration changes (Go `omitempty`). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this audit entry. | 
**action** | **str** | Type of configuration change that was made. | 
**key** | **str** | Configuration key that was changed. | 
**tenant_id** | **str** | Tenant ID if this was a tenant-scoped change, null for global changes. | [optional] 
**old_value** | **object** | Previous value before the change, null for create actions. | [optional] 
**new_value** | **object** | New value after the change, null for delete actions. | [optional] 
**changed_by** | **str** | User ID of the person who made the change. | 
**timestamp** | **datetime** | ISO 8601 timestamp when the change occurred. | 

## Example

```python
from aqueduct_sdk.models.config_audit_entry import ConfigAuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAuditEntry from a JSON string
config_audit_entry_instance = ConfigAuditEntry.from_json(json)
# print the JSON string representation of the object
print(ConfigAuditEntry.to_json())

# convert the object into a dict
config_audit_entry_dict = config_audit_entry_instance.to_dict()
# create an instance of ConfigAuditEntry from a dict
config_audit_entry_from_dict = ConfigAuditEntry.from_dict(config_audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


