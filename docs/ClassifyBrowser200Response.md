# ClassifyBrowser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**os** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**is_bot** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.classify_browser200_response import ClassifyBrowser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyBrowser200Response from a JSON string
classify_browser200_response_instance = ClassifyBrowser200Response.from_json(json)
# print the JSON string representation of the object
print(ClassifyBrowser200Response.to_json())

# convert the object into a dict
classify_browser200_response_dict = classify_browser200_response_instance.to_dict()
# create an instance of ClassifyBrowser200Response from a dict
classify_browser200_response_from_dict = ClassifyBrowser200Response.from_dict(classify_browser200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


