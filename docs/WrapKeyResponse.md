# WrapKeyResponse

Response containing the wrapped Data Encryption Key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wrapped_dek** | **str** | Base64-encoded wrapped DEK. | 

## Example

```python
from aqueduct_sdk.models.wrap_key_response import WrapKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WrapKeyResponse from a JSON string
wrap_key_response_instance = WrapKeyResponse.from_json(json)
# print the JSON string representation of the object
print(WrapKeyResponse.to_json())

# convert the object into a dict
wrap_key_response_dict = wrap_key_response_instance.to_dict()
# create an instance of WrapKeyResponse from a dict
wrap_key_response_from_dict = WrapKeyResponse.from_dict(wrap_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


