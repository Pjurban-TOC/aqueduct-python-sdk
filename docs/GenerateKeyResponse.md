# GenerateKeyResponse

Response containing metadata for the newly generated HSM key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**HSMKeyMetadata**](HSMKeyMetadata.md) |  | 

## Example

```python
from aqueduct_sdk.models.generate_key_response import GenerateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateKeyResponse from a JSON string
generate_key_response_instance = GenerateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateKeyResponse.to_json())

# convert the object into a dict
generate_key_response_dict = generate_key_response_instance.to_dict()
# create an instance of GenerateKeyResponse from a dict
generate_key_response_from_dict = GenerateKeyResponse.from_dict(generate_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


