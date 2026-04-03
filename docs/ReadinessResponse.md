# ReadinessResponse

Readiness probe response indicating dependency health.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**checks** | [**Dict[str, ReadinessResponseChecksValue]**](ReadinessResponseChecksValue.md) | Health status of each dependency. | 

## Example

```python
from aqueduct_sdk.models.readiness_response import ReadinessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadinessResponse from a JSON string
readiness_response_instance = ReadinessResponse.from_json(json)
# print the JSON string representation of the object
print(ReadinessResponse.to_json())

# convert the object into a dict
readiness_response_dict = readiness_response_instance.to_dict()
# create an instance of ReadinessResponse from a dict
readiness_response_from_dict = ReadinessResponse.from_dict(readiness_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


