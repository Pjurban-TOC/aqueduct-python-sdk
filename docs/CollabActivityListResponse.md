# CollabActivityListResponse

Paginated list of collaboration activity records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[CollabActivityRecord]**](CollabActivityRecord.md) |  | 
**next_cursor** | **str** | Opaque cursor for the next page. Absent when no more results. | [optional] 

## Example

```python
from aqueduct_sdk.models.collab_activity_list_response import CollabActivityListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollabActivityListResponse from a JSON string
collab_activity_list_response_instance = CollabActivityListResponse.from_json(json)
# print the JSON string representation of the object
print(CollabActivityListResponse.to_json())

# convert the object into a dict
collab_activity_list_response_dict = collab_activity_list_response_instance.to_dict()
# create an instance of CollabActivityListResponse from a dict
collab_activity_list_response_from_dict = CollabActivityListResponse.from_dict(collab_activity_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


