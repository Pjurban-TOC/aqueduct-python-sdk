# UpdateConfigRequest

Request body for updating tenant configuration. Matches `tenants.go:95` UpdateConfigRequest. All fields are optional — only provided fields are updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_timeout_minutes** | **int** |  | [optional] 
**mfa_required** | **bool** |  | [optional] 
**ip_allowlist** | **List[str]** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.update_config_request import UpdateConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigRequest from a JSON string
update_config_request_instance = UpdateConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConfigRequest.to_json())

# convert the object into a dict
update_config_request_dict = update_config_request_instance.to_dict()
# create an instance of UpdateConfigRequest from a dict
update_config_request_from_dict = UpdateConfigRequest.from_dict(update_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


