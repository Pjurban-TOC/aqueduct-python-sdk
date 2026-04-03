# AuditLogEntryRag

RAG retrieval context for this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **bool** |  | [optional] 
**knowledge_base_id** | **str** |  | [optional] 
**chunks_retrieved** | **int** |  | [optional] 
**retrieval_score** | **float** | Average relevance score of retrieved chunks. | [optional] 
**search_time_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_rag import AuditLogEntryRag

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryRag from a JSON string
audit_log_entry_rag_instance = AuditLogEntryRag.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryRag.to_json())

# convert the object into a dict
audit_log_entry_rag_dict = audit_log_entry_rag_instance.to_dict()
# create an instance of AuditLogEntryRag from a dict
audit_log_entry_rag_from_dict = AuditLogEntryRag.from_dict(audit_log_entry_rag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


