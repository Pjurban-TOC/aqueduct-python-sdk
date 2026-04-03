# RevokeTokenRequest

Token revocation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token to revoke. | 
**reason** | **str** | Reason for revoking the token. | 

## Example

```python
from aqueduct_sdk.models.revoke_token_request import RevokeTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeTokenRequest from a JSON string
revoke_token_request_instance = RevokeTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeTokenRequest.to_json())

# convert the object into a dict
revoke_token_request_dict = revoke_token_request_instance.to_dict()
# create an instance of RevokeTokenRequest from a dict
revoke_token_request_from_dict = RevokeTokenRequest.from_dict(revoke_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


