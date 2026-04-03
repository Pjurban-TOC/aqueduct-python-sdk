# ComplianceEvidence

A piece of evidence supporting a compliance check result. Matches compliance-engine ComplianceEvidence struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique evidence identifier. | 
**source_type** | **str** | Type of source that produced this evidence (e.g., audit_log, config, scan). | 
**event_id** | **str** | Identifier of the originating event or resource. | 
**tenant_id** | **str** | Tenant to which this evidence belongs. | 
**timestamp** | **datetime** | Timestamp when the evidence was recorded (ISO 8601). | 
**summary** | **str** | Brief human-readable summary of the evidence. | 
**details** | **Dict[str, object]** | Arbitrary key-value details specific to the evidence source. | 

## Example

```python
from aqueduct_sdk.models.compliance_evidence import ComplianceEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceEvidence from a JSON string
compliance_evidence_instance = ComplianceEvidence.from_json(json)
# print the JSON string representation of the object
print(ComplianceEvidence.to_json())

# convert the object into a dict
compliance_evidence_dict = compliance_evidence_instance.to_dict()
# create an instance of ComplianceEvidence from a dict
compliance_evidence_from_dict = ComplianceEvidence.from_dict(compliance_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


