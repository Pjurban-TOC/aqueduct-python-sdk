# ReadinessResponseChecksValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**latency_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.readiness_response_checks_value import ReadinessResponseChecksValue

# TODO update the JSON string below
json = "{}"
# create an instance of ReadinessResponseChecksValue from a JSON string
readiness_response_checks_value_instance = ReadinessResponseChecksValue.from_json(json)
# print the JSON string representation of the object
print(ReadinessResponseChecksValue.to_json())

# convert the object into a dict
readiness_response_checks_value_dict = readiness_response_checks_value_instance.to_dict()
# create an instance of ReadinessResponseChecksValue from a dict
readiness_response_checks_value_from_dict = ReadinessResponseChecksValue.from_dict(readiness_response_checks_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


