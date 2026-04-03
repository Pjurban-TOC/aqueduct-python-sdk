# DeletionRequestResponse

Response confirming creation of a deletion request with timeline and approval requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_request_id** | **str** | Unique identifier for this deletion request. | 
**tenant_id** | **str** | Tenant targeted for deletion. | 
**status** | **str** | Current status of the deletion request. | 
**requires_approval** | **bool** | Whether the request needs explicit admin approval before proceeding. | 
**approvers_required** | **int** | Number of distinct admin approvals required. | 
**soft_delete_at** | **datetime** | Scheduled timestamp for soft deletion (data marked but not purged). | 
**hard_delete_at** | **datetime** | Scheduled timestamp for permanent data purge. | 
**export_url** | **str** | Pre-signed URL for the data export, or null if not yet ready. | [optional] 

## Example

```python
from aqueduct_sdk.models.deletion_request_response import DeletionRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionRequestResponse from a JSON string
deletion_request_response_instance = DeletionRequestResponse.from_json(json)
# print the JSON string representation of the object
print(DeletionRequestResponse.to_json())

# convert the object into a dict
deletion_request_response_dict = deletion_request_response_instance.to_dict()
# create an instance of DeletionRequestResponse from a dict
deletion_request_response_from_dict = DeletionRequestResponse.from_dict(deletion_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


