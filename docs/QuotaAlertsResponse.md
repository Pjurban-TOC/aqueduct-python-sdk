# QuotaAlertsResponse

List of quota alerts. Matches `quotas.go:148` QuotaAlertsResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[QuotaAlertDetail]**](QuotaAlertDetail.md) |  | 

## Example

```python
from aqueduct_sdk.models.quota_alerts_response import QuotaAlertsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaAlertsResponse from a JSON string
quota_alerts_response_instance = QuotaAlertsResponse.from_json(json)
# print the JSON string representation of the object
print(QuotaAlertsResponse.to_json())

# convert the object into a dict
quota_alerts_response_dict = quota_alerts_response_instance.to_dict()
# create an instance of QuotaAlertsResponse from a dict
quota_alerts_response_from_dict = QuotaAlertsResponse.from_dict(quota_alerts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


