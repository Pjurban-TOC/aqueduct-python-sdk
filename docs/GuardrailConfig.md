# GuardrailConfig

Guardrail configuration defining input and output safety rails. Per LlamaFirewall multi-layer architecture. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guardrail_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**input_rails** | [**List[SafetyRail]**](SafetyRail.md) | Safety checks applied to user input before model routing. | 
**output_rails** | [**List[SafetyRail]**](SafetyRail.md) | Safety checks applied to model output before returning to user. | 
**reasoning_rails** | [**List[SafetyRail]**](SafetyRail.md) | Safety checks applied to intermediate reasoning steps. Per LlamaFirewall reasoning-guard layer.  | [optional] 
**mode** | **str** | Default execution mode per OneShield [arXiv:2507.21170]. | [optional] [default to 'sequential']
**enabled** | **bool** |  | [optional] [default to True]
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.guardrail_config import GuardrailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GuardrailConfig from a JSON string
guardrail_config_instance = GuardrailConfig.from_json(json)
# print the JSON string representation of the object
print(GuardrailConfig.to_json())

# convert the object into a dict
guardrail_config_dict = guardrail_config_instance.to_dict()
# create an instance of GuardrailConfig from a dict
guardrail_config_from_dict = GuardrailConfig.from_dict(guardrail_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


