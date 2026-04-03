# ConditionResponse

A condition as returned in API responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**operator** | **str** |  | 
**value** | **object** | The value to compare against. | 

## Example

```python
from aqueduct_sdk.models.condition_response import ConditionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionResponse from a JSON string
condition_response_instance = ConditionResponse.from_json(json)
# print the JSON string representation of the object
print(ConditionResponse.to_json())

# convert the object into a dict
condition_response_dict = condition_response_instance.to_dict()
# create an instance of ConditionResponse from a dict
condition_response_from_dict = ConditionResponse.from_dict(condition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


