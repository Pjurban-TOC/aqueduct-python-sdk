# QuotaStatusResponse

Tenant quota status. Matches `quotas.go:70` QuotaStatusResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** | Current plan tier. | 
**limits** | [**Dict[str, QuotaLimit]**](QuotaLimit.md) | Map of resource name to quota limit details. | 
**models_allowed** | **List[str]** | List of AI models available to this tenant. | 
**features_enabled** | **List[str]** | List of enabled platform features. | 
**alerts** | [**List[QuotaAlertSummary]**](QuotaAlertSummary.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.quota_status_response import QuotaStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaStatusResponse from a JSON string
quota_status_response_instance = QuotaStatusResponse.from_json(json)
# print the JSON string representation of the object
print(QuotaStatusResponse.to_json())

# convert the object into a dict
quota_status_response_dict = quota_status_response_instance.to_dict()
# create an instance of QuotaStatusResponse from a dict
quota_status_response_from_dict = QuotaStatusResponse.from_dict(quota_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


