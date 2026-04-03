# TestSubscriptionResponse

Result of sending a test webhook.test event to a subscription endpoint. Maps to service.TestResult. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the endpoint returned a 2xx status code. | 
**status_code** | **int** | HTTP status code returned by the subscriber endpoint. | 
**latency_ms** | **int** | Round-trip latency in milliseconds. | 
**error** | **str** | Error message if the test failed. | [optional] 

## Example

```python
from aqueduct_sdk.models.test_subscription_response import TestSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestSubscriptionResponse from a JSON string
test_subscription_response_instance = TestSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(TestSubscriptionResponse.to_json())

# convert the object into a dict
test_subscription_response_dict = test_subscription_response_instance.to_dict()
# create an instance of TestSubscriptionResponse from a dict
test_subscription_response_from_dict = TestSubscriptionResponse.from_dict(test_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


