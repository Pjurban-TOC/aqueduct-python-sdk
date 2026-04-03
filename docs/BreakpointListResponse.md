# BreakpointListResponse

Paginated list of breakpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakpoints** | [**List[BreakpointResponse]**](BreakpointResponse.md) |  | 
**total_count** | **int** | Total number of breakpoints matching the filter. | 
**next_cursor** | **str** | Cursor for fetching the next page. Absent when there are no more results. | [optional] 

## Example

```python
from aqueduct_sdk.models.breakpoint_list_response import BreakpointListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BreakpointListResponse from a JSON string
breakpoint_list_response_instance = BreakpointListResponse.from_json(json)
# print the JSON string representation of the object
print(BreakpointListResponse.to_json())

# convert the object into a dict
breakpoint_list_response_dict = breakpoint_list_response_instance.to_dict()
# create an instance of BreakpointListResponse from a dict
breakpoint_list_response_from_dict = BreakpointListResponse.from_dict(breakpoint_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


