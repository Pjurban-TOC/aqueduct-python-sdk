# ComplianceControl

A single control within a compliance framework. Matches compliance-engine ComplianceControl struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique control identifier. | 
**framework_id** | **str** | Parent framework identifier. | 
**name** | **str** | Human-readable control name. | 
**description** | **str** | Detailed description of the control requirements. | 
**category** | **str** | Control category or domain grouping. | 
**check_ids** | **List[str]** | Identifiers of automated checks that evaluate this control. | 

## Example

```python
from aqueduct_sdk.models.compliance_control import ComplianceControl

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceControl from a JSON string
compliance_control_instance = ComplianceControl.from_json(json)
# print the JSON string representation of the object
print(ComplianceControl.to_json())

# convert the object into a dict
compliance_control_dict = compliance_control_instance.to_dict()
# create an instance of ComplianceControl from a dict
compliance_control_from_dict = ComplianceControl.from_dict(compliance_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


