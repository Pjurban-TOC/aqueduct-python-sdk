# DecryptResponse

Response containing the decrypted plaintext.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaintext** | **str** | Base64-encoded decrypted plaintext. | 

## Example

```python
from aqueduct_sdk.models.decrypt_response import DecryptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptResponse from a JSON string
decrypt_response_instance = DecryptResponse.from_json(json)
# print the JSON string representation of the object
print(DecryptResponse.to_json())

# convert the object into a dict
decrypt_response_dict = decrypt_response_instance.to_dict()
# create an instance of DecryptResponse from a dict
decrypt_response_from_dict = DecryptResponse.from_dict(decrypt_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


