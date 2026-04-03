# SafetyRail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**SafetyCheckType**](SafetyCheckType.md) |  | 
**threshold** | **float** | Confidence threshold to trigger this rail. | 
**action** | **str** | Action when the threshold is exceeded. | 
**custom_model** | **str** | Custom model for this specific check (overrides default). | [optional] 

## Example

```python
from aqueduct_sdk.models.safety_rail import SafetyRail

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyRail from a JSON string
safety_rail_instance = SafetyRail.from_json(json)
# print the JSON string representation of the object
print(SafetyRail.to_json())

# convert the object into a dict
safety_rail_dict = safety_rail_instance.to_dict()
# create an instance of SafetyRail from a dict
safety_rail_from_dict = SafetyRail.from_dict(safety_rail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


