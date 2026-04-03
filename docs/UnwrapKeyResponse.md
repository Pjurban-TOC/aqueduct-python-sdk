# UnwrapKeyResponse

Response containing the unwrapped Data Encryption Key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dek** | **str** | Base64-encoded unwrapped DEK. | 

## Example

```python
from aqueduct_sdk.models.unwrap_key_response import UnwrapKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnwrapKeyResponse from a JSON string
unwrap_key_response_instance = UnwrapKeyResponse.from_json(json)
# print the JSON string representation of the object
print(UnwrapKeyResponse.to_json())

# convert the object into a dict
unwrap_key_response_dict = unwrap_key_response_instance.to_dict()
# create an instance of UnwrapKeyResponse from a dict
unwrap_key_response_from_dict = UnwrapKeyResponse.from_dict(unwrap_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


