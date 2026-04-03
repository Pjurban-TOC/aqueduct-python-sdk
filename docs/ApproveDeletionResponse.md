# ApproveDeletionResponse

Response confirming a deletion approval with current approval tally.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Deletion request identifier. | 
**status** | **str** | Updated status of the deletion request. | 
**approvals** | [**List[ApprovalRecord]**](ApprovalRecord.md) | List of recorded approvals for this deletion request. | 
**approvals_remaining** | **int** | Number of additional approvals still required. | 
**deletion_will_proceed** | **bool** | Whether the deletion will proceed (true when all approvals are met). | 

## Example

```python
from aqueduct_sdk.models.approve_deletion_response import ApproveDeletionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveDeletionResponse from a JSON string
approve_deletion_response_instance = ApproveDeletionResponse.from_json(json)
# print the JSON string representation of the object
print(ApproveDeletionResponse.to_json())

# convert the object into a dict
approve_deletion_response_dict = approve_deletion_response_instance.to_dict()
# create an instance of ApproveDeletionResponse from a dict
approve_deletion_response_from_dict = ApproveDeletionResponse.from_dict(approve_deletion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


