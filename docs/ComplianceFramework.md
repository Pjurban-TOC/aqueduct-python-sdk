# ComplianceFramework

A compliance framework definition (e.g., SOC2, HIPAA, FedRAMP). Matches compliance-engine ComplianceFramework struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique framework identifier. | 
**name** | **str** | Human-readable framework name. | 
**version** | **str** | Framework version or revision year. | 
**description** | **str** | Brief summary of the compliance framework scope and purpose. | 
**controls** | [**List[ComplianceControl]**](ComplianceControl.md) | Controls defined within this framework. | 

## Example

```python
from aqueduct_sdk.models.compliance_framework import ComplianceFramework

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceFramework from a JSON string
compliance_framework_instance = ComplianceFramework.from_json(json)
# print the JSON string representation of the object
print(ComplianceFramework.to_json())

# convert the object into a dict
compliance_framework_dict = compliance_framework_instance.to_dict()
# create an instance of ComplianceFramework from a dict
compliance_framework_from_dict = ComplianceFramework.from_dict(compliance_framework_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


