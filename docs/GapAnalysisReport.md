# GapAnalysisReport

Full gap analysis report for a compliance framework against a tenant. Per AEGIS [arXiv:2603.12621] and NIST AI RMF 1.0 continuous monitoring requirements. Matches compliance-engine GapAnalysisReport struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework** | **str** | Framework identifier. | 
**framework_name** | **str** | Human-readable framework name. | 
**tenant_id** | **str** | Tenant for which the gap analysis was performed. | 
**timestamp** | **datetime** | Timestamp when the gap analysis was generated (ISO 8601). | 
**overall_score** | **float** | Overall compliance score as a percentage (0-100). | 
**controls** | [**List[ControlReport]**](ControlReport.md) | Per-control compliance reports. | 
**total_controls** | **int** | Total number of controls evaluated. | 
**met_controls** | **int** | Number of controls with MET status. | 
**unmet_controls** | **int** | Number of controls with UNMET status. | 

## Example

```python
from aqueduct_sdk.models.gap_analysis_report import GapAnalysisReport

# TODO update the JSON string below
json = "{}"
# create an instance of GapAnalysisReport from a JSON string
gap_analysis_report_instance = GapAnalysisReport.from_json(json)
# print the JSON string representation of the object
print(GapAnalysisReport.to_json())

# convert the object into a dict
gap_analysis_report_dict = gap_analysis_report_instance.to_dict()
# create an instance of GapAnalysisReport from a dict
gap_analysis_report_from_dict = GapAnalysisReport.from_dict(gap_analysis_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


