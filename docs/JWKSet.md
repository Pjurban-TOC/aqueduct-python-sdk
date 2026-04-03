# JWKSet

JSON Web Key Set per [RFC 7517](https://www.rfc-editor.org/rfc/rfc7517). Contains the public keys used to verify JWT tokens issued by the auth service. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[JWK]**](JWK.md) |  | 

## Example

```python
from aqueduct_sdk.models.jwk_set import JWKSet

# TODO update the JSON string below
json = "{}"
# create an instance of JWKSet from a JSON string
jwk_set_instance = JWKSet.from_json(json)
# print the JSON string representation of the object
print(JWKSet.to_json())

# convert the object into a dict
jwk_set_dict = jwk_set_instance.to_dict()
# create an instance of JWKSet from a dict
jwk_set_from_dict = JWKSet.from_dict(jwk_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


