# ValidateTokenResponse

Token validation result with decoded claims.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the token is valid and not expired. | 
**sub** | **str** | Subject (user ID) from the token. | [optional] 
**tid** | **str** | Tenant ID from the token claims. | [optional] 
**roles** | **List[str]** | Roles assigned to the user. | [optional] 
**scopes** | **List[str]** | OAuth 2.0 scopes granted to the token. | [optional] 
**jti** | **str** | Unique JWT token identifier. | [optional] 

## Example

```python
from aqueduct_sdk.models.validate_token_response import ValidateTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTokenResponse from a JSON string
validate_token_response_instance = ValidateTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateTokenResponse.to_json())

# convert the object into a dict
validate_token_response_dict = validate_token_response_instance.to_dict()
# create an instance of ValidateTokenResponse from a dict
validate_token_response_from_dict = ValidateTokenResponse.from_dict(validate_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


