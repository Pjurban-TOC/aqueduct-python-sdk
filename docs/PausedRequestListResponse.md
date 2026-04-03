# PausedRequestListResponse

Paginated list of paused requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | [**List[PausedRequestResponse]**](PausedRequestResponse.md) |  | 
**total_count** | **int** | Total number of paused requests matching the filter. | 
**next_cursor** | **str** | Cursor for fetching the next page. | [optional] 

## Example

```python
from aqueduct_sdk.models.paused_request_list_response import PausedRequestListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PausedRequestListResponse from a JSON string
paused_request_list_response_instance = PausedRequestListResponse.from_json(json)
# print the JSON string representation of the object
print(PausedRequestListResponse.to_json())

# convert the object into a dict
paused_request_list_response_dict = paused_request_list_response_instance.to_dict()
# create an instance of PausedRequestListResponse from a dict
paused_request_list_response_from_dict = PausedRequestListResponse.from_dict(paused_request_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


