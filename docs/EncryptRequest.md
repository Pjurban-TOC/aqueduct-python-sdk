# EncryptRequest

Request to encrypt data using an HSM key (AES-256-GCM per NIST SP 800-38D).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Identifier of the encryption key. | 
**plaintext** | **str** | Base64-encoded plaintext to encrypt. | 
**aad** | **str** | Additional authenticated data per NIST SP 800-38D. | [optional] 

## Example

```python
from aqueduct_sdk.models.encrypt_request import EncryptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptRequest from a JSON string
encrypt_request_instance = EncryptRequest.from_json(json)
# print the JSON string representation of the object
print(EncryptRequest.to_json())

# convert the object into a dict
encrypt_request_dict = encrypt_request_instance.to_dict()
# create an instance of EncryptRequest from a dict
encrypt_request_from_dict = EncryptRequest.from_dict(encrypt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


