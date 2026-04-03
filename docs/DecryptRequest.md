# DecryptRequest

Request to decrypt data using an HSM key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Identifier of the decryption key. | 
**ciphertext** | **str** | Base64-encoded ciphertext to decrypt. | 
**nonce** | **str** | Base64-encoded 96-bit GCM nonce used during encryption. | 
**aad** | **str** | Additional authenticated data that was provided during encryption. | [optional] 

## Example

```python
from aqueduct_sdk.models.decrypt_request import DecryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptRequest from a JSON string
decrypt_request_instance = DecryptRequest.from_json(json)
# print the JSON string representation of the object
print(DecryptRequest.to_json())

# convert the object into a dict
decrypt_request_dict = decrypt_request_instance.to_dict()
# create an instance of DecryptRequest from a dict
decrypt_request_from_dict = DecryptRequest.from_dict(decrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


