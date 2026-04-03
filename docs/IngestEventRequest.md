# IngestEventRequest

Request body for POST /api/v1/webhooks/events. Maps to service.IngestEventRequest. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Canonical event type to ingest. | 
**payload** | **object** | Arbitrary JSON payload for the event. | 
**idempotency_key** | **str** | Optional client-supplied idempotency key.  If omitted the server computes one from SHA-256(tenant_id + event_type + payload).  | [optional] 

## Example

```python
from aqueduct_sdk.models.ingest_event_request import IngestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IngestEventRequest from a JSON string
ingest_event_request_instance = IngestEventRequest.from_json(json)
# print the JSON string representation of the object
print(IngestEventRequest.to_json())

# convert the object into a dict
ingest_event_request_dict = ingest_event_request_instance.to_dict()
# create an instance of IngestEventRequest from a dict
ingest_event_request_from_dict = IngestEventRequest.from_dict(ingest_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


