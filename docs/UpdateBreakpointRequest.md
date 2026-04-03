# UpdateBreakpointRequest

Request body for updating an existing breakpoint. All fields except `version` are optional; only supplied fields are changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name (2-100 characters). | [optional] 
**description** | **str** | Updated description. | [optional] 
**stage** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**conditions** | [**List[ConditionRequest]**](ConditionRequest.md) |  | [optional] 
**priority** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**version** | **int** | Current version of the breakpoint (for optimistic locking). Must match the server&#39;s version. | 

## Example

```python
from aqueduct_sdk.models.update_breakpoint_request import UpdateBreakpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBreakpointRequest from a JSON string
update_breakpoint_request_instance = UpdateBreakpointRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateBreakpointRequest.to_json())

# convert the object into a dict
update_breakpoint_request_dict = update_breakpoint_request_instance.to_dict()
# create an instance of UpdateBreakpointRequest from a dict
update_breakpoint_request_from_dict = UpdateBreakpointRequest.from_dict(update_breakpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


