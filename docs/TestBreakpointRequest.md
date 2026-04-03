# TestBreakpointRequest

Request body for testing a breakpoint against sample field data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **Dict[str, object]** | Map of field names to values used to evaluate the breakpoint conditions. | 

## Example

```python
from aqueduct_sdk.models.test_breakpoint_request import TestBreakpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestBreakpointRequest from a JSON string
test_breakpoint_request_instance = TestBreakpointRequest.from_json(json)
# print the JSON string representation of the object
print(TestBreakpointRequest.to_json())

# convert the object into a dict
test_breakpoint_request_dict = test_breakpoint_request_instance.to_dict()
# create an instance of TestBreakpointRequest from a dict
test_breakpoint_request_from_dict = TestBreakpointRequest.from_dict(test_breakpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


