# CreateBreakpointRequest

Request body for creating a new breakpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Tenant that owns this breakpoint, or \&quot;*\&quot; for global. | 
**name** | **str** | Human-readable name (2-100 characters). | 
**description** | **str** | Longer explanation of the breakpoint&#39;s purpose. | 
**stage** | **str** | Pipeline stage where the breakpoint is evaluated. | 
**mode** | **str** | Action to take when all conditions match. | 
**conditions** | [**List[ConditionRequest]**](ConditionRequest.md) | Flat list of conditions — all must match for the breakpoint to trigger. At least one required. | 
**priority** | **str** | Priority level. | 

## Example

```python
from aqueduct_sdk.models.create_breakpoint_request import CreateBreakpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBreakpointRequest from a JSON string
create_breakpoint_request_instance = CreateBreakpointRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBreakpointRequest.to_json())

# convert the object into a dict
create_breakpoint_request_dict = create_breakpoint_request_instance.to_dict()
# create an instance of CreateBreakpointRequest from a dict
create_breakpoint_request_from_dict = CreateBreakpointRequest.from_dict(create_breakpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


