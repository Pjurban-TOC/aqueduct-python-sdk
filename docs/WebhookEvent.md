# WebhookEvent

An inbound event stored by the webhook service and dispatched to matching subscriptions.  Maps to types.WebhookEvent. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique event identifier. | 
**tenant_id** | **str** | Owning tenant. | 
**event_type** | **str** | Canonical event type. | 
**payload** | **object** | Event-specific JSON payload. | 
**payload_size** | **int** | Size of the payload in bytes. | 
**idempotency_key** | **str** | Client-supplied or server-computed SHA-256 idempotency key.  | 
**created_at** | **datetime** | Timestamp when the event was ingested. | 

## Example

```python
from aqueduct_sdk.models.webhook_event import WebhookEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEvent from a JSON string
webhook_event_instance = WebhookEvent.from_json(json)
# print the JSON string representation of the object
print(WebhookEvent.to_json())

# convert the object into a dict
webhook_event_dict = webhook_event_instance.to_dict()
# create an instance of WebhookEvent from a dict
webhook_event_from_dict = WebhookEvent.from_dict(webhook_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


