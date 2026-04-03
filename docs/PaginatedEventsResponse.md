# PaginatedEventsResponse

Paginated events response. Matches handler/common.go PaginatedResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActivityEvent]**](ActivityEvent.md) |  | 
**pagination** | [**PaginatedEventsResponsePagination**](PaginatedEventsResponsePagination.md) |  | 

## Example

```python
from aqueduct_sdk.models.paginated_events_response import PaginatedEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventsResponse from a JSON string
paginated_events_response_instance = PaginatedEventsResponse.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventsResponse.to_json())

# convert the object into a dict
paginated_events_response_dict = paginated_events_response_instance.to_dict()
# create an instance of PaginatedEventsResponse from a dict
paginated_events_response_from_dict = PaginatedEventsResponse.from_dict(paginated_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


