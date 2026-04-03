# DeletionRequestSummary

Abbreviated deletion request details for status responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Deletion request identifier. | 
**requested_by** | **str** | User ID of the requester. | 
**requested_at** | **datetime** | Timestamp when the deletion was requested. | 
**reason** | **str** | Categorized reason for the deletion. | 

## Example

```python
from aqueduct_sdk.models.deletion_request_summary import DeletionRequestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionRequestSummary from a JSON string
deletion_request_summary_instance = DeletionRequestSummary.from_json(json)
# print the JSON string representation of the object
print(DeletionRequestSummary.to_json())

# convert the object into a dict
deletion_request_summary_dict = deletion_request_summary_instance.to_dict()
# create an instance of DeletionRequestSummary from a dict
deletion_request_summary_from_dict = DeletionRequestSummary.from_dict(deletion_request_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


