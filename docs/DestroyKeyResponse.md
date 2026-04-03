# DestroyKeyResponse

Response confirming key destruction. FIPS 140-3 zeroization ensures no key material remains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the destruction and zeroization succeeded. | 
**key_id** | **str** | Identifier of the destroyed key. | 

## Example

```python
from aqueduct_sdk.models.destroy_key_response import DestroyKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DestroyKeyResponse from a JSON string
destroy_key_response_instance = DestroyKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DestroyKeyResponse.to_json())

# convert the object into a dict
destroy_key_response_dict = destroy_key_response_instance.to_dict()
# create an instance of DestroyKeyResponse from a dict
destroy_key_response_from_dict = DestroyKeyResponse.from_dict(destroy_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


