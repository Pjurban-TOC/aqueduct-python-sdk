# UpdateSubscriptionRequest

Request body for PUT /api/v1/webhooks/subscriptions/{id}. All fields are optional — only supplied fields are updated. Maps to service.UpdateSubscriptionRequest. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | New HTTPS endpoint URL. | [optional] 
**event_types** | **List[str]** | Replacement set of event types. | [optional] 
**headers** | **Dict[str, str]** | Replacement custom headers. | [optional] 
**description** | **str** | Updated human-readable description. | [optional] 
**active** | **bool** | Enable or disable the subscription. | [optional] 
**max_retries** | **int** | Updated max delivery retry attempts. | [optional] 
**timeout_sec** | **int** | Updated HTTP timeout in seconds. | [optional] 
**rate_limit_rpm** | **int** | Updated rate limit (requests per minute). 0 &#x3D; unlimited. | [optional] 

## Example

```python
from aqueduct_sdk.models.update_subscription_request import UpdateSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionRequest from a JSON string
update_subscription_request_instance = UpdateSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionRequest.to_json())

# convert the object into a dict
update_subscription_request_dict = update_subscription_request_instance.to_dict()
# create an instance of UpdateSubscriptionRequest from a dict
update_subscription_request_from_dict = UpdateSubscriptionRequest.from_dict(update_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


