# DeadLetterEntry

A permanently failed delivery stored in the dead-letter queue for manual review and optional replay.  Maps to types.DeadLetterEntry. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique DLQ entry identifier. | 
**tenant_id** | **str** | Owning tenant. | 
**subscription_id** | **str** | Target subscription that failed. | 
**delivery_id** | **str** | Correlation ID to the original delivery attempt. | 
**event_id** | **str** | Source event. | 
**event_type** | **str** | Event type of the original event. | 
**url** | **str** | Destination URL that was called. | 
**payload** | **object** | Original event payload preserved for replay. | 
**attempt_count** | **int** | Total delivery attempts before dead-lettering. | 
**last_response_code** | **int** | HTTP status code from the last failed attempt. | 
**last_error** | **str** | Error from the last failed attempt. | 
**created_at** | **datetime** | When the original delivery was created. | 
**dead_lettered_at** | **datetime** | When the entry was moved to the dead-letter queue. | 
**replayed_at** | **datetime** | When the entry was replayed (null if not yet replayed). | [optional] 

## Example

```python
from aqueduct_sdk.models.dead_letter_entry import DeadLetterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DeadLetterEntry from a JSON string
dead_letter_entry_instance = DeadLetterEntry.from_json(json)
# print the JSON string representation of the object
print(DeadLetterEntry.to_json())

# convert the object into a dict
dead_letter_entry_dict = dead_letter_entry_instance.to_dict()
# create an instance of DeadLetterEntry from a dict
dead_letter_entry_from_dict = DeadLetterEntry.from_dict(dead_letter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


