# AuditLogEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**path** | **str** |  | 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**content_length** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_request import AuditLogEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryRequest from a JSON string
audit_log_entry_request_instance = AuditLogEntryRequest.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryRequest.to_json())

# convert the object into a dict
audit_log_entry_request_dict = audit_log_entry_request_instance.to_dict()
# create an instance of AuditLogEntryRequest from a dict
audit_log_entry_request_from_dict = AuditLogEntryRequest.from_dict(audit_log_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


