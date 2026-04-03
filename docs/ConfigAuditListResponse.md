# ConfigAuditListResponse

Paginated list of configuration audit log entries. Matches `config.go` ConfigAuditListResponse struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ConfigAuditEntry]**](ConfigAuditEntry.md) | Array of audit log entries, newest first. | 
**next_cursor** | **str** | Cursor for the next page. Empty when no more results. | [optional] 
**total** | **int** | Total number of audit entries matching the query. | 

## Example

```python
from aqueduct_sdk.models.config_audit_list_response import ConfigAuditListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAuditListResponse from a JSON string
config_audit_list_response_instance = ConfigAuditListResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigAuditListResponse.to_json())

# convert the object into a dict
config_audit_list_response_dict = config_audit_list_response_instance.to_dict()
# create an instance of ConfigAuditListResponse from a dict
config_audit_list_response_from_dict = ConfigAuditListResponse.from_dict(config_audit_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


