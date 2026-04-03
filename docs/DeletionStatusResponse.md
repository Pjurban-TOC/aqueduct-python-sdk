# DeletionStatusResponse

Comprehensive deletion status for a tenant including request, approvals, timeline, and export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier. | 
**deletion_status** | **str** | Current deletion lifecycle stage. | 
**request** | [**DeletionRequestSummary**](DeletionRequestSummary.md) | Summary of the deletion request, or null if no request exists. | [optional] 
**approvals** | [**List[ApprovalRecord]**](ApprovalRecord.md) | List of approvals recorded for this deletion request. | 
**timeline** | [**DeletionTimeline**](DeletionTimeline.md) | Deletion timeline milestones, or null if no deletion is scheduled. | [optional] 
**export** | [**ExportSummary**](ExportSummary.md) | Data export summary, or null if no export was requested. | [optional] 

## Example

```python
from aqueduct_sdk.models.deletion_status_response import DeletionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionStatusResponse from a JSON string
deletion_status_response_instance = DeletionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DeletionStatusResponse.to_json())

# convert the object into a dict
deletion_status_response_dict = deletion_status_response_instance.to_dict()
# create an instance of DeletionStatusResponse from a dict
deletion_status_response_from_dict = DeletionStatusResponse.from_dict(deletion_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


