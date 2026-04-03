# ListDeadLetterEntriesResponse

Paginated list of dead-letter queue entries. Handler returns: {\"entries\":[], \"next_cursor\":\"\", \"has_more\":bool} 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[DeadLetterEntry]**](DeadLetterEntry.md) |  | 
**next_cursor** | **str** | Opaque cursor for the next page. Empty string when no more pages. | 
**has_more** | **bool** | True when additional pages exist. | 

## Example

```python
from aqueduct_sdk.models.list_dead_letter_entries_response import ListDeadLetterEntriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeadLetterEntriesResponse from a JSON string
list_dead_letter_entries_response_instance = ListDeadLetterEntriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDeadLetterEntriesResponse.to_json())

# convert the object into a dict
list_dead_letter_entries_response_dict = list_dead_letter_entries_response_instance.to_dict()
# create an instance of ListDeadLetterEntriesResponse from a dict
list_dead_letter_entries_response_from_dict = ListDeadLetterEntriesResponse.from_dict(list_dead_letter_entries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


