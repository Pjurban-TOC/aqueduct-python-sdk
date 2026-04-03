# BreakpointResponse

A breakpoint configuration as returned by the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique breakpoint identifier. | 
**tenant_id** | **str** | Tenant that owns this breakpoint, or \&quot;*\&quot; for global. | 
**name** | **str** | Human-readable breakpoint name (2-100 characters). | 
**description** | **str** | Longer explanation of the breakpoint&#39;s purpose. | 
**stage** | **str** | Pipeline stage where the breakpoint is evaluated. | 
**mode** | **str** | Action taken when all conditions match. | 
**conditions** | [**List[ConditionResponse]**](ConditionResponse.md) | Flat list of conditions — all must match for the breakpoint to trigger. | 
**priority** | **str** | Priority level as a string label. | 
**enabled** | **bool** | Whether the breakpoint is currently active. | 
**created_by** | **str** | User who created the breakpoint. | 
**created_at** | **datetime** | Timestamp when the breakpoint was created. | 
**updated_at** | **datetime** | Timestamp of the last update. | 
**version** | **int** | Optimistic-lock version counter. | 

## Example

```python
from aqueduct_sdk.models.breakpoint_response import BreakpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BreakpointResponse from a JSON string
breakpoint_response_instance = BreakpointResponse.from_json(json)
# print the JSON string representation of the object
print(BreakpointResponse.to_json())

# convert the object into a dict
breakpoint_response_dict = breakpoint_response_instance.to_dict()
# create an instance of BreakpointResponse from a dict
breakpoint_response_from_dict = BreakpointResponse.from_dict(breakpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


