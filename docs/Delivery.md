# Delivery

A single delivery attempt for an event+subscription pair. Maps to types.DeliveryAttempt. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique delivery identifier. | 
**tenant_id** | **str** | Owning tenant. | 
**subscription_id** | **str** | Target subscription. | 
**event_id** | **str** | Source event. | 
**event_type** | **str** | Event type of the source event. | 
**url** | **str** | Destination URL that was called. | 
**status** | **str** | Current delivery lifecycle state. | 
**attempt_count** | **int** | Number of delivery attempts made so far. | 
**max_retries** | **int** | Maximum retry attempts configured at dispatch time. | 
**next_retry_at** | **datetime** | Scheduled time for the next retry attempt. | [optional] 
**last_attempt_at** | **datetime** | Timestamp of the most recent attempt. | [optional] 
**response_status** | **int** | HTTP status code returned by the subscriber endpoint. | [optional] 
**response_body** | **str** | Truncated response body (max 1 KB). | [optional] 
**error_message** | **str** | Error message if the attempt failed. | [optional] 
**created_at** | **datetime** | When this delivery record was created. | 
**completed_at** | **datetime** | When the delivery reached a terminal state. | [optional] 

## Example

```python
from aqueduct_sdk.models.delivery import Delivery

# TODO update the JSON string below
json = "{}"
# create an instance of Delivery from a JSON string
delivery_instance = Delivery.from_json(json)
# print the JSON string representation of the object
print(Delivery.to_json())

# convert the object into a dict
delivery_dict = delivery_instance.to_dict()
# create an instance of Delivery from a dict
delivery_from_dict = Delivery.from_dict(delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


