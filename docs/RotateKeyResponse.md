# RotateKeyResponse

Response containing metadata for the newly rotated HSM key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_key** | [**HSMKeyMetadata**](HSMKeyMetadata.md) |  | 

## Example

```python
from aqueduct_sdk.models.rotate_key_response import RotateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RotateKeyResponse from a JSON string
rotate_key_response_instance = RotateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RotateKeyResponse.to_json())

# convert the object into a dict
rotate_key_response_dict = rotate_key_response_instance.to_dict()
# create an instance of RotateKeyResponse from a dict
rotate_key_response_from_dict = RotateKeyResponse.from_dict(rotate_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


