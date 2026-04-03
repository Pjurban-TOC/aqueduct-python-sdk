# ReviewResultResponse

Result returned after a review action (approve, reject, or modify).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | ID of the reviewed paused request. | 
**decision** | **str** | The review decision. | 
**reviewed_by** | **str** | User who performed the review. | 
**reviewed_at** | **datetime** | Timestamp of the review. | 
**message** | **str** | Human-readable result message. | 

## Example

```python
from aqueduct_sdk.models.review_result_response import ReviewResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewResultResponse from a JSON string
review_result_response_instance = ReviewResultResponse.from_json(json)
# print the JSON string representation of the object
print(ReviewResultResponse.to_json())

# convert the object into a dict
review_result_response_dict = review_result_response_instance.to_dict()
# create an instance of ReviewResultResponse from a dict
review_result_response_from_dict = ReviewResultResponse.from_dict(review_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


