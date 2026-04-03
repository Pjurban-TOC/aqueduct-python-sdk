# ModelInfoCapabilities

Model capability flags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | **bool** |  | [optional] 
**embeddings** | **bool** |  | [optional] 
**function_calling** | **bool** |  | [optional] 
**vision** | **bool** |  | [optional] 
**streaming** | **bool** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.model_info_capabilities import ModelInfoCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInfoCapabilities from a JSON string
model_info_capabilities_instance = ModelInfoCapabilities.from_json(json)
# print the JSON string representation of the object
print(ModelInfoCapabilities.to_json())

# convert the object into a dict
model_info_capabilities_dict = model_info_capabilities_instance.to_dict()
# create an instance of ModelInfoCapabilities from a dict
model_info_capabilities_from_dict = ModelInfoCapabilities.from_dict(model_info_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


