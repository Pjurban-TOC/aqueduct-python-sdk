# ConfigEntry

A configuration entry stored in the config-service KV store. Matches `config.go` ConfigEntry struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Dot-separated configuration key. | 
**value** | **object** | Configuration value. Type depends on the &#x60;type&#x60; field. | 
**type** | **str** | Data type of the configuration value. | 
**description** | **str** | Human-readable description of what this configuration controls. | [optional] 
**version** | **int** | Monotonically increasing version number, incremented on each update. | [optional] 
**updated_at** | **datetime** | ISO 8601 timestamp of the last update. | [optional] 
**updated_by** | **str** | User ID of the last person who modified this entry. | [optional] 

## Example

```python
from aqueduct_sdk.models.config_entry import ConfigEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigEntry from a JSON string
config_entry_instance = ConfigEntry.from_json(json)
# print the JSON string representation of the object
print(ConfigEntry.to_json())

# convert the object into a dict
config_entry_dict = config_entry_instance.to_dict()
# create an instance of ConfigEntry from a dict
config_entry_from_dict = ConfigEntry.from_dict(config_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


