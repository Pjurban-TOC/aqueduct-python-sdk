# ConfigVersionListResponse

Paginated list of configuration version history entries. Matches `config.go` ConfigVersionListResponse struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**List[ConfigVersion]**](ConfigVersion.md) | Array of version history records, newest first. | 
**next_cursor** | **str** | Cursor for the next page. Empty when no more results. | [optional] 
**total** | **int** | Total number of versions for this configuration key. | 

## Example

```python
from aqueduct_sdk.models.config_version_list_response import ConfigVersionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigVersionListResponse from a JSON string
config_version_list_response_instance = ConfigVersionListResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigVersionListResponse.to_json())

# convert the object into a dict
config_version_list_response_dict = config_version_list_response_instance.to_dict()
# create an instance of ConfigVersionListResponse from a dict
config_version_list_response_from_dict = ConfigVersionListResponse.from_dict(config_version_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


