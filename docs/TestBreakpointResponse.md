# TestBreakpointResponse

Result of testing a breakpoint against sample fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**triggered** | **bool** | Whether all conditions matched (breakpoint would fire). | 
**matched_conditions** | **List[int]** | Zero-based indices of the conditions that matched. | 
**message** | **str** | Human-readable summary of the test result. | 

## Example

```python
from aqueduct_sdk.models.test_breakpoint_response import TestBreakpointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestBreakpointResponse from a JSON string
test_breakpoint_response_instance = TestBreakpointResponse.from_json(json)
# print the JSON string representation of the object
print(TestBreakpointResponse.to_json())

# convert the object into a dict
test_breakpoint_response_dict = test_breakpoint_response_instance.to_dict()
# create an instance of TestBreakpointResponse from a dict
test_breakpoint_response_from_dict = TestBreakpointResponse.from_dict(test_breakpoint_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


