# ApprovalRecord

A single admin approval entry in the deletion approval chain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved_by** | **str** | User ID of the approving administrator. | 
**approved_at** | **datetime** | Timestamp when the approval was recorded. | 

## Example

```python
from aqueduct_sdk.models.approval_record import ApprovalRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalRecord from a JSON string
approval_record_instance = ApprovalRecord.from_json(json)
# print the JSON string representation of the object
print(ApprovalRecord.to_json())

# convert the object into a dict
approval_record_dict = approval_record_instance.to_dict()
# create an instance of ApprovalRecord from a dict
approval_record_from_dict = ApprovalRecord.from_dict(approval_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


