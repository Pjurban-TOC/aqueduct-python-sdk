# CreateSubscriptionRequest

Request body for POST /api/v1/webhooks/subscriptions. Maps to service.CreateSubscriptionRequest. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | HTTPS endpoint URL to receive webhook deliveries. | 
**event_types** | **List[str]** | Event types to subscribe to (at least one required). | 
**headers** | **Dict[str, str]** | Custom headers included in every delivery.  Reserved Standard Webhooks headers (webhook-id, webhook-timestamp, webhook-signature, content-type, user-agent) are rejected.  | [optional] 
**description** | **str** | Human-readable description of this subscription. | [optional] 
**max_retries** | **int** | Maximum delivery retry attempts. Server defaults to 5 when omitted or &lt;&#x3D; 0. | [optional] 
**timeout_sec** | **int** | HTTP request timeout in seconds. Server defaults to 30 when omitted or &lt;&#x3D; 0. | [optional] 
**rate_limit_rpm** | **int** | Maximum deliveries per minute. 0 means unlimited. | [optional] 

## Example

```python
from aqueduct_sdk.models.create_subscription_request import CreateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequest from a JSON string
create_subscription_request_instance = CreateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequest.to_json())

# convert the object into a dict
create_subscription_request_dict = create_subscription_request_instance.to_dict()
# create an instance of CreateSubscriptionRequest from a dict
create_subscription_request_from_dict = CreateSubscriptionRequest.from_dict(create_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


