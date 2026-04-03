# SSLStatus

SSL certificate state for a custom domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | SSL provisioning status. | [optional] 
**issued_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**issuer** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.ssl_status import SSLStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SSLStatus from a JSON string
ssl_status_instance = SSLStatus.from_json(json)
# print the JSON string representation of the object
print(SSLStatus.to_json())

# convert the object into a dict
ssl_status_dict = ssl_status_instance.to_dict()
# create an instance of SSLStatus from a dict
ssl_status_from_dict = SSLStatus.from_dict(ssl_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


