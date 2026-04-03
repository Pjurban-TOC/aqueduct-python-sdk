# CreateSubscription201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique subscription identifier. | 
**tenant_id** | **str** | Owning tenant. | 
**url** | **str** | Destination URL for deliveries. | 
**secret** | **str** | Signing secret — store securely, only returned once. | [optional] 
**event_types** | **List[str]** | Event types this subscription receives. | 
**headers** | **Dict[str, str]** | Custom headers sent with every delivery. | [optional] 
**active** | **bool** | Whether the subscription is currently active. | 
**description** | **str** | Human-readable description. | [optional] 
**max_retries** | **int** | Maximum delivery retry attempts. | 
**timeout_sec** | **int** | HTTP request timeout in seconds. | 
**rate_limit_rpm** | **int** | Deliveries per minute limit. 0 &#x3D; unlimited. | 
**created_at** | **datetime** | When the subscription was created. | 
**updated_at** | **datetime** | When the subscription was last modified. | 
**previous_secret** | **str** | Previous signing secret kept during zero-downtime rotation grace period.  Never exposed via the API (always empty in responses).  | [optional] 
**previous_secret_expires_at** | **datetime** | Expiry of the rotation grace period. | [optional] 

## Example

```python
from aqueduct_sdk.models.create_subscription201_response import CreateSubscription201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscription201Response from a JSON string
create_subscription201_response_instance = CreateSubscription201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSubscription201Response.to_json())

# convert the object into a dict
create_subscription201_response_dict = create_subscription201_response_instance.to_dict()
# create an instance of CreateSubscription201Response from a dict
create_subscription201_response_from_dict = CreateSubscription201Response.from_dict(create_subscription201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


