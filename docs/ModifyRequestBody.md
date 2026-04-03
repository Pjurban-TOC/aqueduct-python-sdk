# ModifyRequestBody

Request body for modifying a paused request before approving it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifications** | **Dict[str, object]** | Key-value modifications to apply to the request before forwarding. | 
**notes** | **str** | Optional notes from the reviewer. | [optional] 

## Example

```python
from aqueduct_sdk.models.modify_request_body import ModifyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ModifyRequestBody from a JSON string
modify_request_body_instance = ModifyRequestBody.from_json(json)
# print the JSON string representation of the object
print(ModifyRequestBody.to_json())

# convert the object into a dict
modify_request_body_dict = modify_request_body_instance.to_dict()
# create an instance of ModifyRequestBody from a dict
modify_request_body_from_dict = ModifyRequestBody.from_dict(modify_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


