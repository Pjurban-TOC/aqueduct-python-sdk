# CreateConfigRequest

Request body for creating a new configuration entry. Matches `config.go` CreateConfigRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Dot-separated configuration key. Must match &#x60;^[a-zA-Z0-9._-]+$&#x60;. | 
**value** | **object** | Configuration value to set. Must be compatible with the specified type. | 
**type** | **str** | Data type of the configuration value. | 
**description** | **str** | Human-readable description of what this configuration controls. | [optional] 

## Example

```python
from aqueduct_sdk.models.create_config_request import CreateConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigRequest from a JSON string
create_config_request_instance = CreateConfigRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConfigRequest.to_json())

# convert the object into a dict
create_config_request_dict = create_config_request_instance.to_dict()
# create an instance of CreateConfigRequest from a dict
create_config_request_from_dict = CreateConfigRequest.from_dict(create_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


