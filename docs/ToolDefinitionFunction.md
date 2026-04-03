# ToolDefinitionFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**parameters** | **object** | JSON Schema for function parameters. | [optional] 

## Example

```python
from aqueduct_sdk.models.tool_definition_function import ToolDefinitionFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ToolDefinitionFunction from a JSON string
tool_definition_function_instance = ToolDefinitionFunction.from_json(json)
# print the JSON string representation of the object
print(ToolDefinitionFunction.to_json())

# convert the object into a dict
tool_definition_function_dict = tool_definition_function_instance.to_dict()
# create an instance of ToolDefinitionFunction from a dict
tool_definition_function_from_dict = ToolDefinitionFunction.from_dict(tool_definition_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


