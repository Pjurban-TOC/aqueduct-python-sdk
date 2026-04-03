# CheckResult

Result of a single compliance check execution. Matches compliance-engine CheckResult struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | Identifier of the check that was executed. | 
**tenant_id** | **str** | Tenant against which the check was run. | 
**status** | [**ControlStatus**](ControlStatus.md) |  | 
**message** | **str** | Human-readable result message explaining the check outcome. | 
**evidence** | [**List[ComplianceEvidence]**](ComplianceEvidence.md) | Supporting evidence collected during the check. | 
**checked_at** | **datetime** | Timestamp when the check was executed (ISO 8601). | 

## Example

```python
from aqueduct_sdk.models.check_result import CheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResult from a JSON string
check_result_instance = CheckResult.from_json(json)
# print the JSON string representation of the object
print(CheckResult.to_json())

# convert the object into a dict
check_result_dict = check_result_instance.to_dict()
# create an instance of CheckResult from a dict
check_result_from_dict = CheckResult.from_dict(check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


