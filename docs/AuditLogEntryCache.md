# AuditLogEntryCache

Semantic cache status for this request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_hit** | **bool** |  | [optional] 
**semantic_similarity_score** | **float** | Similarity score to cached query (if evaluated). | [optional] 
**cache_key** | **str** | Cache key hash (for debugging, not the actual content). | [optional] 

## Example

```python
from aqueduct_sdk.models.audit_log_entry_cache import AuditLogEntryCache

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogEntryCache from a JSON string
audit_log_entry_cache_instance = AuditLogEntryCache.from_json(json)
# print the JSON string representation of the object
print(AuditLogEntryCache.to_json())

# convert the object into a dict
audit_log_entry_cache_dict = audit_log_entry_cache_instance.to_dict()
# create an instance of AuditLogEntryCache from a dict
audit_log_entry_cache_from_dict = AuditLogEntryCache.from_dict(audit_log_entry_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


