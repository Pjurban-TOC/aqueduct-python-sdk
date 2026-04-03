# HSMHealthResponse

HSM subsystem health and FIPS 140-3 self-test status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** | Whether the service has an active connection to the HSM. | 
**self_test_passed** | **bool** | Whether the FIPS 140-3 power-on self-test passed. | 
**provider_id** | **str** | HSM provider or partition identifier. | 
**available_sessions** | **int** | Number of available PKCS#11 sessions in the pool. | 
**active_key_count** | **int** | Number of keys in active state on this HSM. | 
**latency_ms** | **float** | Round-trip latency to the HSM in milliseconds. | 
**firmware_version** | **str** | HSM firmware version string. | 

## Example

```python
from aqueduct_sdk.models.hsm_health_response import HSMHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HSMHealthResponse from a JSON string
hsm_health_response_instance = HSMHealthResponse.from_json(json)
# print the JSON string representation of the object
print(HSMHealthResponse.to_json())

# convert the object into a dict
hsm_health_response_dict = hsm_health_response_instance.to_dict()
# create an instance of HSMHealthResponse from a dict
hsm_health_response_from_dict = HSMHealthResponse.from_dict(hsm_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


