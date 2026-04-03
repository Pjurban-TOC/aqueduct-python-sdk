# AuditLogEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** |  | [optional] 
**content_length** | **int** |  | [optional] 
**error_code** | **str** | Error code if the response was an error. | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_response import AuditLogEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryResponse from a JSON string
audit_log_entry_response_instance = AuditLogEntryResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryResponse.to_json())

# convert the object into a dict
audit_log_entry_response_dict = audit_log_entry_response_instance.to_dict()
# create an instance of AuditLogEntryResponse from a dict
audit_log_entry_response_from_dict = AuditLogEntryResponse.from_dict(audit_log_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


