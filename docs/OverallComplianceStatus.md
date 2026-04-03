# OverallComplianceStatus

Aggregated compliance status across all frameworks for a tenant. Per ISpec [arXiv:2512.17259] multi-framework compliance overview. Matches compliance-engine OverallComplianceStatus struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant identifier. | 
**frameworks** | [**List[FrameworkStatus]**](FrameworkStatus.md) | Per-framework compliance status summaries. | 

## Example

```python
from aqueduct_sdk.models.overall_compliance_status import OverallComplianceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OverallComplianceStatus from a JSON string
overall_compliance_status_instance = OverallComplianceStatus.from_json(json)
# print the JSON string representation of the object
print(OverallComplianceStatus.to_json())

# convert the object into a dict
overall_compliance_status_dict = overall_compliance_status_instance.to_dict()
# create an instance of OverallComplianceStatus from a dict
overall_compliance_status_from_dict = OverallComplianceStatus.from_dict(overall_compliance_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


