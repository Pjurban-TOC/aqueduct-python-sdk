# SafetyFinding

Single safety check finding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_type** | [**SafetyCheckType**](SafetyCheckType.md) |  | 
**detected** | **bool** | Whether this check detected a violation. | 
**score** | **float** | Confidence score for this detection. | 
**severity** | **str** |  | [optional] 
**category** | **str** | Sub-category within the check type. | [optional] 
**evidence** | **str** | Excerpt of the content that triggered detection. | [optional] 
**explanation** | **str** | Human-readable explanation of why this was flagged. | [optional] 

## Example

```python
from aqueduct_sdk.models.safety_finding import SafetyFinding

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyFinding from a JSON string
safety_finding_instance = SafetyFinding.from_json(json)
# print the JSON string representation of the object
print(SafetyFinding.to_json())

# convert the object into a dict
safety_finding_dict = safety_finding_instance.to_dict()
# create an instance of SafetyFinding from a dict
safety_finding_from_dict = SafetyFinding.from_dict(safety_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


