# RunComplianceCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework_id** | **str** | Framework to check against. | 
**tenant_id** | **str** | Tenant to evaluate. | 
**control_id** | **str** | Specific control to check (optional; omit to check all). | [optional] 

## Example

```python
from aqueduct_sdk.models.run_compliance_check_request import RunComplianceCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunComplianceCheckRequest from a JSON string
run_compliance_check_request_instance = RunComplianceCheckRequest.from_json(json)
# print the JSON string representation of the object
print(RunComplianceCheckRequest.to_json())

# convert the object into a dict
run_compliance_check_request_dict = run_compliance_check_request_instance.to_dict()
# create an instance of RunComplianceCheckRequest from a dict
run_compliance_check_request_from_dict = RunComplianceCheckRequest.from_dict(run_compliance_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


