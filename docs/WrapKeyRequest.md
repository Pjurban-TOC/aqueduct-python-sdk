# WrapKeyRequest

Request to wrap a Data Encryption Key using AES-KWP (RFC 5649 / NIST SP 800-38F).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kek_id** | **str** | Key Encryption Key ID. | 
**dek** | **str** | Data Encryption Key to wrap. | 

## Example

```python
from aqueduct_sdk.models.wrap_key_request import WrapKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WrapKeyRequest from a JSON string
wrap_key_request_instance = WrapKeyRequest.from_json(json)
# print the JSON string representation of the object
print(WrapKeyRequest.to_json())

# convert the object into a dict
wrap_key_request_dict = wrap_key_request_instance.to_dict()
# create an instance of WrapKeyRequest from a dict
wrap_key_request_from_dict = WrapKeyRequest.from_dict(wrap_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


