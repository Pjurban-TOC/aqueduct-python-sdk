# AuditLogQueryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[AuditLogEntry]**](AuditLogEntry.md) |  | 
**next_cursor** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**aggregations** | [**AuditLogQueryResponseAggregations**](AuditLogQueryResponseAggregations.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_query_response import AuditLogQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogQueryResponse from a JSON string
audit_log_query_response_instance = AuditLogQueryResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogQueryResponse.to_json())

# convert the object into a dict
audit_log_query_response_dict = audit_log_query_response_instance.to_dict()
# create an instance of AuditLogQueryResponse from a dict
audit_log_query_response_from_dict = AuditLogQueryResponse.from_dict(audit_log_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


