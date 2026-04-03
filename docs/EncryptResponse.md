# EncryptResponse

Response containing the ciphertext produced by HSM encryption.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | **str** | Base64-encoded ciphertext. | 
**nonce** | **str** | 96-bit GCM nonce per NIST SP 800-38D. | 
**key_id** | **str** | Identifier of the key used for encryption. | 
**key_version** | **int** | Version of the key used for encryption (incremented on rotation). | 

## Example

```python
from aqueduct_sdk.models.encrypt_response import EncryptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptResponse from a JSON string
encrypt_response_instance = EncryptResponse.from_json(json)
# print the JSON string representation of the object
print(EncryptResponse.to_json())

# convert the object into a dict
encrypt_response_dict = encrypt_response_instance.to_dict()
# create an instance of EncryptResponse from a dict
encrypt_response_from_dict = EncryptResponse.from_dict(encrypt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


