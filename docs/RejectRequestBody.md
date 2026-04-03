# RejectRequestBody

Request body for rejecting a paused request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Rejection reason (required). | 

## Example

```python
from aqueduct_sdk.models.reject_request_body import RejectRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RejectRequestBody from a JSON string
reject_request_body_instance = RejectRequestBody.from_json(json)
# print the JSON string representation of the object
print(RejectRequestBody.to_json())

# convert the object into a dict
reject_request_body_dict = reject_request_body_instance.to_dict()
# create an instance of RejectRequestBody from a dict
reject_request_body_from_dict = RejectRequestBody.from_dict(reject_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


