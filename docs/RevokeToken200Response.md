# RevokeToken200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revoked** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.revoke_token200_response import RevokeToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeToken200Response from a JSON string
revoke_token200_response_instance = RevokeToken200Response.from_json(json)
# print the JSON string representation of the object
print(RevokeToken200Response.to_json())

# convert the object into a dict
revoke_token200_response_dict = revoke_token200_response_instance.to_dict()
# create an instance of RevokeToken200Response from a dict
revoke_token200_response_from_dict = RevokeToken200Response.from_dict(revoke_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


