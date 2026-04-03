# GetBrowserCapabilities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_features** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_browser_capabilities200_response import GetBrowserCapabilities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrowserCapabilities200Response from a JSON string
get_browser_capabilities200_response_instance = GetBrowserCapabilities200Response.from_json(json)
# print the JSON string representation of the object
print(GetBrowserCapabilities200Response.to_json())

# convert the object into a dict
get_browser_capabilities200_response_dict = get_browser_capabilities200_response_instance.to_dict()
# create an instance of GetBrowserCapabilities200Response from a dict
get_browser_capabilities200_response_from_dict = GetBrowserCapabilities200Response.from_dict(get_browser_capabilities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


