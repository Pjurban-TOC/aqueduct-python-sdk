# DeactivateKeyResponse

Response confirming key deactivation per NIST SP 800-57 state transition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the deactivation succeeded. | 
**key_id** | **str** | Identifier of the deactivated key. | 

## Example

```python
from aqueduct_sdk.models.deactivate_key_response import DeactivateKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateKeyResponse from a JSON string
deactivate_key_response_instance = DeactivateKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DeactivateKeyResponse.to_json())

# convert the object into a dict
deactivate_key_response_dict = deactivate_key_response_instance.to_dict()
# create an instance of DeactivateKeyResponse from a dict
deactivate_key_response_from_dict = DeactivateKeyResponse.from_dict(deactivate_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


