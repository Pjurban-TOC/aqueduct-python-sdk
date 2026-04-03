# PausedRequestResponse

A request that was paused by a breakpoint, awaiting operator review.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the paused request. | 
**breakpoint_id** | **str** | ID of the breakpoint that triggered the pause. | 
**breakpoint_name** | **str** | Human-readable name of the triggering breakpoint. | [optional] 
**tenant_id** | **str** |  | 
**user_id** | **str** | User whose request was paused. | 
**correlation_id** | **str** | Correlation ID for distributed tracing. | 
**stage** | **str** | Pipeline stage where the request was paused. | 
**priority** | **str** | Priority level of the paused request. | 
**sanitized_preview** | **str** | DLP-sanitized preview of the request content for safe operator review. | 
**metadata** | **Dict[str, object]** | Optional key-value metadata attached to the paused request. | [optional] 
**status** | **str** | Current review status. | 
**paused_at** | **datetime** | Timestamp when the request was paused. | 
**expires_at** | **datetime** | Timestamp when the paused request will auto-expire if not reviewed. | 
**reviewed_by** | **str** | User who reviewed the request. | [optional] 
**review_decision** | **str** | The review decision (approved, rejected, modified_approved). | [optional] 
**review_notes** | **str** | Notes provided by the reviewer. | [optional] 
**reviewed_at** | **datetime** | Timestamp of the review. Null/absent if not yet reviewed. | [optional] 

## Example

```python
from aqueduct_sdk.models.paused_request_response import PausedRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PausedRequestResponse from a JSON string
paused_request_response_instance = PausedRequestResponse.from_json(json)
# print the JSON string representation of the object
print(PausedRequestResponse.to_json())

# convert the object into a dict
paused_request_response_dict = paused_request_response_instance.to_dict()
# create an instance of PausedRequestResponse from a dict
paused_request_response_from_dict = PausedRequestResponse.from_dict(paused_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


