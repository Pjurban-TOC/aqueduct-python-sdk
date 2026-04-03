# ActivityEvent

Activity event. Matches domain/event.go ActivityEvent struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event identifier (format &#x60;evt_{random12}&#x60;). | 
**tenant_id** | **str** |  | 
**user_id** | **str** |  | 
**timestamp** | **datetime** |  | 
**action** | **str** | Action performed (e.g., document.view, auth.login). | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**outcome** | **str** | Action outcome. | 
**error_code** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**hash_chain** | **str** | Integrity hash chain value. | 
**previous_hash** | **str** |  | [optional] 
**storage_tier** | **str** | Storage tier (hot or cold). | 
**archived_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.activity_event import ActivityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityEvent from a JSON string
activity_event_instance = ActivityEvent.from_json(json)
# print the JSON string representation of the object
print(ActivityEvent.to_json())

# convert the object into a dict
activity_event_dict = activity_event_instance.to_dict()
# create an instance of ActivityEvent from a dict
activity_event_from_dict = ActivityEvent.from_dict(activity_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


