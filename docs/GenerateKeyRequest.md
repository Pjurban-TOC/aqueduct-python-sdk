# GenerateKeyRequest

Request to generate a new HSM-managed key. Matches `handler.go` GenerateKeyRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_type** | [**HSMKeyType**](HSMKeyType.md) |  | 
**label** | **str** | Human-readable label for the new key. | 

## Example

```python
from aqueduct_sdk.models.generate_key_request import GenerateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateKeyRequest from a JSON string
generate_key_request_instance = GenerateKeyRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateKeyRequest.to_json())

# convert the object into a dict
generate_key_request_dict = generate_key_request_instance.to_dict()
# create an instance of GenerateKeyRequest from a dict
generate_key_request_from_dict = GenerateKeyRequest.from_dict(generate_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


