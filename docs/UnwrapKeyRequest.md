# UnwrapKeyRequest

Request to unwrap a Data Encryption Key using AES-KWP (RFC 5649 / NIST SP 800-38F).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kek_id** | **str** | Key Encryption Key ID. | 
**wrapped_dek** | **str** | Base64-encoded wrapped DEK to unwrap. | 

## Example

```python
from aqueduct_sdk.models.unwrap_key_request import UnwrapKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnwrapKeyRequest from a JSON string
unwrap_key_request_instance = UnwrapKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UnwrapKeyRequest.to_json())

# convert the object into a dict
unwrap_key_request_dict = unwrap_key_request_instance.to_dict()
# create an instance of UnwrapKeyRequest from a dict
unwrap_key_request_from_dict = UnwrapKeyRequest.from_dict(unwrap_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


