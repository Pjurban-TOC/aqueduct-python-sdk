# ConfigVersion

A single version record from the configuration version history. Matches `config.go` ConfigVersion struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Configuration key this version belongs to. | 
**version** | **int** | Version number for this snapshot. | 
**value** | **object** | The configuration value at this version. | 
**timestamp** | **datetime** | ISO 8601 timestamp when this version was created. | 
**changed_by** | **str** | User ID of the person who created this version. | 
**reason** | **str** | Optional reason or changelog note for this version change. | [optional] 

## Example

```python
from aqueduct_sdk.models.config_version import ConfigVersion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigVersion from a JSON string
config_version_instance = ConfigVersion.from_json(json)
# print the JSON string representation of the object
print(ConfigVersion.to_json())

# convert the object into a dict
config_version_dict = config_version_instance.to_dict()
# create an instance of ConfigVersion from a dict
config_version_from_dict = ConfigVersion.from_dict(config_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


