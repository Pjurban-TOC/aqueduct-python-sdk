# Session

Active user session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Unique session identifier. | 
**user_id** | **str** | User ID that owns this session. | 
**tenant_id** | **str** | Tenant this session belongs to. | 
**access_token_jti** | **str** | JTI of the current access token bound to this session. | 
**refresh_token_hash** | **str** | Hash of the current refresh token for this session. | 
**created_at** | **datetime** | When the session was created. | 
**expires_at** | **datetime** | Absolute session expiration time. | 
**last_active_at** | **datetime** | Last time activity was recorded on this session. | 
**ip_address** | **str** | IP address of the session origin. | 
**user_agent** | **str** | Browser/client user agent string. | 
**mfa_verified** | **bool** | Whether MFA was completed for this session. | 
**revoked** | **bool** | Whether this session has been revoked. | 
**revoked_reason** | **str** | Reason the session was revoked, if applicable. | [optional] 
**dpop_key_thumbprint** | **str** | DPoP key thumbprint for sender-constrained tokens (RFC 9449). | [optional] 

## Example

```python
from aqueduct_sdk.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


