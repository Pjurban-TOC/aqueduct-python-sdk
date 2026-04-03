# CreateGuardrailConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**input_rails** | [**List[SafetyRail]**](SafetyRail.md) |  | 
**output_rails** | [**List[SafetyRail]**](SafetyRail.md) |  | 
**reasoning_rails** | [**List[SafetyRail]**](SafetyRail.md) |  | [optional] 
**mode** | **str** |  | [optional] [default to 'sequential']
**enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from aqueduct_sdk.models.create_guardrail_config_request import CreateGuardrailConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuardrailConfigRequest from a JSON string
create_guardrail_config_request_instance = CreateGuardrailConfigRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuardrailConfigRequest.to_json())

# convert the object into a dict
create_guardrail_config_request_dict = create_guardrail_config_request_instance.to_dict()
# create an instance of CreateGuardrailConfigRequest from a dict
create_guardrail_config_request_from_dict = CreateGuardrailConfigRequest.from_dict(create_guardrail_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


