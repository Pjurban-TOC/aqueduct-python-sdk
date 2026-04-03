# ConfigUpdateConfigRequest

Request body for updating an existing configuration entry. Matches `config.go` UpdateConfigRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | New configuration value. Must be compatible with the entry&#39;s type. | 
**type** | **str** | Optionally change the data type of this configuration entry. | [optional] 
**description** | **str** | Updated human-readable description. | [optional] 

## Example

```python
from aqueduct_sdk.models.config_update_config_request import ConfigUpdateConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigUpdateConfigRequest from a JSON string
config_update_config_request_instance = ConfigUpdateConfigRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigUpdateConfigRequest.to_json())

# convert the object into a dict
config_update_config_request_dict = config_update_config_request_instance.to_dict()
# create an instance of ConfigUpdateConfigRequest from a dict
config_update_config_request_from_dict = ConfigUpdateConfigRequest.from_dict(config_update_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


