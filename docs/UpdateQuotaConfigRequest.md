# UpdateQuotaConfigRequest

Admin request to update quota configuration. Matches `quotas.go:95` UpdateQuotaConfigRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**QuotaLimitsUpdate**](QuotaLimitsUpdate.md) |  | [optional] 
**models_allowed** | **List[str]** |  | [optional] 
**features_enabled** | **List[str]** |  | [optional] 
**temporary_increase** | [**TemporaryIncreaseReq**](TemporaryIncreaseReq.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.update_quota_config_request import UpdateQuotaConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuotaConfigRequest from a JSON string
update_quota_config_request_instance = UpdateQuotaConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuotaConfigRequest.to_json())

# convert the object into a dict
update_quota_config_request_dict = update_quota_config_request_instance.to_dict()
# create an instance of UpdateQuotaConfigRequest from a dict
update_quota_config_request_from_dict = UpdateQuotaConfigRequest.from_dict(update_quota_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


