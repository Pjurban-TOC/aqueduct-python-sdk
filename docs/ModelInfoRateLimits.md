# ModelInfoRateLimits

Per-model rate limits for the requesting tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpm** | **int** | Requests per minute. | [optional] 
**tpm** | **int** | Tokens per minute. | [optional] 

## Example

```python
from aqueduct_sdk.models.model_info_rate_limits import ModelInfoRateLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInfoRateLimits from a JSON string
model_info_rate_limits_instance = ModelInfoRateLimits.from_json(json)
# print the JSON string representation of the object
print(ModelInfoRateLimits.to_json())

# convert the object into a dict
model_info_rate_limits_dict = model_info_rate_limits_instance.to_dict()
# create an instance of ModelInfoRateLimits from a dict
model_info_rate_limits_from_dict = ModelInfoRateLimits.from_dict(model_info_rate_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


