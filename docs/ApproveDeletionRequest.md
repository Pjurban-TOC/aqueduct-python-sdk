# ApproveDeletionRequest

Request body for approving a tenant deletion request. Requires system admin scope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_confirmation** | **str** | Must match \&quot;APPROVE DELETE {tenant_name}\&quot; to confirm approval. | 

## Example

```python
from aqueduct_sdk.models.approve_deletion_request import ApproveDeletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveDeletionRequest from a JSON string
approve_deletion_request_instance = ApproveDeletionRequest.from_json(json)
# print the JSON string representation of the object
print(ApproveDeletionRequest.to_json())

# convert the object into a dict
approve_deletion_request_dict = approve_deletion_request_instance.to_dict()
# create an instance of ApproveDeletionRequest from a dict
approve_deletion_request_from_dict = ApproveDeletionRequest.from_dict(approve_deletion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


