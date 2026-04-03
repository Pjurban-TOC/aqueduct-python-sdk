# ConfigListResponse

Paginated list of configuration entries. Matches `config.go` ConfigListResponse struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[ConfigEntry]**](ConfigEntry.md) | Array of configuration entries matching the query. | 
**next_cursor** | **str** | Cursor for the next page. Empty when no more results. | [optional] 
**total** | **int** | Total number of configuration entries matching the query. | 

## Example

```python
from aqueduct_sdk.models.config_list_response import ConfigListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigListResponse from a JSON string
config_list_response_instance = ConfigListResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigListResponse.to_json())

# convert the object into a dict
config_list_response_dict = config_list_response_instance.to_dict()
# create an instance of ConfigListResponse from a dict
config_list_response_from_dict = ConfigListResponse.from_dict(config_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


