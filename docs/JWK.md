# JWK

A single JSON Web Key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key type (RSA, EC). | 
**use** | **str** | Key use (sig &#x3D; signature). | 
**kid** | **str** | Key ID for matching against the JWT header &#x60;kid&#x60; claim. | 
**alg** | **str** | Algorithm (RS256, ES256). | 
**n** | **str** | RSA modulus (Base64url-encoded). | [optional] 
**e** | **str** | RSA exponent (Base64url-encoded). | [optional] 
**x5c** | **List[str]** | X.509 certificate chain. | [optional] 
**x5t** | **str** | X.509 certificate SHA-1 thumbprint (Base64url-encoded). | [optional] 

## Example

```python
from aqueduct_sdk.models.jwk import JWK

# TODO update the JSON string below
json = "{}"
# create an instance of JWK from a JSON string
jwk_instance = JWK.from_json(json)
# print the JSON string representation of the object
print(JWK.to_json())

# convert the object into a dict
jwk_dict = jwk_instance.to_dict()
# create an instance of JWK from a dict
jwk_from_dict = JWK.from_dict(jwk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


