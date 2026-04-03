# UpdateQuotaConfigResponse

Response for quota config update. Matches `quotas.go:118` UpdateQuotaConfigResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** |  | 
**updated_by** | **str** | User ID of the administrator who made the change. | 
**changes** | [**List[QuotaConfigChange]**](QuotaConfigChange.md) |  | 

## Example

```python
from aqueduct_sdk.models.update_quota_config_response import UpdateQuotaConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuotaConfigResponse from a JSON string
update_quota_config_response_instance = UpdateQuotaConfigResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateQuotaConfigResponse.to_json())

# convert the object into a dict
update_quota_config_response_dict = update_quota_config_response_instance.to_dict()
# create an instance of UpdateQuotaConfigResponse from a dict
update_quota_config_response_from_dict = UpdateQuotaConfigResponse.from_dict(update_quota_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


