# ControlReport

Report for a single control within a gap analysis. Matches compliance-engine ControlReport struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Control identifier. | 
**name** | **str** | Human-readable control name. | 
**category** | **str** | Control category or domain grouping. | 
**status** | [**ControlStatus**](ControlStatus.md) |  | 
**checks** | [**List[CheckResult]**](CheckResult.md) | Individual check results for this control. | 
**gaps** | **List[str]** | Identified gaps preventing full compliance (optional, present when status is UNMET or PARTIAL). | [optional] 
**evidence_count** | **int** | Total number of evidence items collected for this control. | 
**last_checked** | **datetime** | Timestamp of the most recent check execution (ISO 8601). | 

## Example

```python
from aqueduct_sdk.models.control_report import ControlReport

# TODO update the JSON string below
json = "{}"
# create an instance of ControlReport from a JSON string
control_report_instance = ControlReport.from_json(json)
# print the JSON string representation of the object
print(ControlReport.to_json())

# convert the object into a dict
control_report_dict = control_report_instance.to_dict()
# create an instance of ControlReport from a dict
control_report_from_dict = ControlReport.from_dict(control_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


