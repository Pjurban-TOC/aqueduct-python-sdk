# QuotaConfigChange

Single config change. Matches `quotas.go:125` QuotaConfigChange.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field path that was changed. | 
**old_value** | **object** |  | 
**new_value** | **object** |  | 

## Example

```python
from aqueduct_sdk.models.quota_config_change import QuotaConfigChange

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaConfigChange from a JSON string
quota_config_change_instance = QuotaConfigChange.from_json(json)
# print the JSON string representation of the object
print(QuotaConfigChange.to_json())

# convert the object into a dict
quota_config_change_dict = quota_config_change_instance.to_dict()
# create an instance of QuotaConfigChange from a dict
quota_config_change_from_dict = QuotaConfigChange.from_dict(quota_config_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


