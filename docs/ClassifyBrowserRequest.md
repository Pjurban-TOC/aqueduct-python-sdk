# ClassifyBrowserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | **str** | Browser User-Agent string to classify. | 

## Example

```python
from aqueduct_sdk.models.classify_browser_request import ClassifyBrowserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClassifyBrowserRequest from a JSON string
classify_browser_request_instance = ClassifyBrowserRequest.from_json(json)
# print the JSON string representation of the object
print(ClassifyBrowserRequest.to_json())

# convert the object into a dict
classify_browser_request_dict = classify_browser_request_instance.to_dict()
# create an instance of ClassifyBrowserRequest from a dict
classify_browser_request_from_dict = ClassifyBrowserRequest.from_dict(classify_browser_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


