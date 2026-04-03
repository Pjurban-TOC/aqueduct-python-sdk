# ListGuardrailConfigs200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guardrails** | [**List[GuardrailConfig]**](GuardrailConfig.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_guardrail_configs200_response import ListGuardrailConfigs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGuardrailConfigs200Response from a JSON string
list_guardrail_configs200_response_instance = ListGuardrailConfigs200Response.from_json(json)
# print the JSON string representation of the object
print(ListGuardrailConfigs200Response.to_json())

# convert the object into a dict
list_guardrail_configs200_response_dict = list_guardrail_configs200_response_instance.to_dict()
# create an instance of ListGuardrailConfigs200Response from a dict
list_guardrail_configs200_response_from_dict = ListGuardrailConfigs200Response.from_dict(list_guardrail_configs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


