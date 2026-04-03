# FlagEvaluationResponse

Result of evaluating a feature flag, including tenant overrides. Matches `config.go` FlagEvaluationResponse struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flag** | **str** | Name of the evaluated feature flag. | 
**enabled** | **bool** | Effective state of the flag after applying tenant overrides. | 

## Example

```python
from aqueduct_sdk.models.flag_evaluation_response import FlagEvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FlagEvaluationResponse from a JSON string
flag_evaluation_response_instance = FlagEvaluationResponse.from_json(json)
# print the JSON string representation of the object
print(FlagEvaluationResponse.to_json())

# convert the object into a dict
flag_evaluation_response_dict = flag_evaluation_response_instance.to_dict()
# create an instance of FlagEvaluationResponse from a dict
flag_evaluation_response_from_dict = FlagEvaluationResponse.from_dict(flag_evaluation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


