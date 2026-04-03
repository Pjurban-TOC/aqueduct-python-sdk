# SignRequest

Request to sign a digest using an HSM signing key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Identifier of the signing key. | 
**digest** | **str** | Base64-encoded digest (hash) to sign. | 

## Example

```python
from aqueduct_sdk.models.sign_request import SignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignRequest from a JSON string
sign_request_instance = SignRequest.from_json(json)
# print the JSON string representation of the object
print(SignRequest.to_json())

# convert the object into a dict
sign_request_dict = sign_request_instance.to_dict()
# create an instance of SignRequest from a dict
sign_request_from_dict = SignRequest.from_dict(sign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


