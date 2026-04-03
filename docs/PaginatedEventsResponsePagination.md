# PaginatedEventsResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** |  | [optional] 
**has_more** | **bool** |  | 
**total** | **int** |  | [optional] 
**page_size** | **int** |  | 

## Example

```python
from aqueduct_sdk.models.paginated_events_response_pagination import PaginatedEventsResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventsResponsePagination from a JSON string
paginated_events_response_pagination_instance = PaginatedEventsResponsePagination.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventsResponsePagination.to_json())

# convert the object into a dict
paginated_events_response_pagination_dict = paginated_events_response_pagination_instance.to_dict()
# create an instance of PaginatedEventsResponsePagination from a dict
paginated_events_response_pagination_from_dict = PaginatedEventsResponsePagination.from_dict(paginated_events_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


