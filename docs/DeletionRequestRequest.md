# DeletionRequestRequest

Request body for initiating tenant deletion per GDPR Art. 17 right to erasure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Categorized reason for the deletion request. | 
**details** | **str** | Additional context for the deletion request. | [optional] 
**confirmation** | **str** | Must match \&quot;DELETE {tenant_name}\&quot; to confirm intent. | 
**export_data** | **bool** | When true, a data export is generated before deletion begins. | [optional] 

## Example

```python
from aqueduct_sdk.models.deletion_request_request import DeletionRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionRequestRequest from a JSON string
deletion_request_request_instance = DeletionRequestRequest.from_json(json)
# print the JSON string representation of the object
print(DeletionRequestRequest.to_json())

# convert the object into a dict
deletion_request_request_dict = deletion_request_request_instance.to_dict()
# create an instance of DeletionRequestRequest from a dict
deletion_request_request_from_dict = DeletionRequestRequest.from_dict(deletion_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


