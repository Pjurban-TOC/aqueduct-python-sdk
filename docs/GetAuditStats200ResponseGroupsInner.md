# GetAuditStats200ResponseGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**total_requests** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 
**total_cost_usd** | **float** |  | [optional] 
**error_rate** | **float** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_audit_stats200_response_groups_inner import GetAuditStats200ResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditStats200ResponseGroupsInner from a JSON string
get_audit_stats200_response_groups_inner_instance = GetAuditStats200ResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print(GetAuditStats200ResponseGroupsInner.to_json())

# convert the object into a dict
get_audit_stats200_response_groups_inner_dict = get_audit_stats200_response_groups_inner_instance.to_dict()
# create an instance of GetAuditStats200ResponseGroupsInner from a dict
get_audit_stats200_response_groups_inner_from_dict = GetAuditStats200ResponseGroupsInner.from_dict(get_audit_stats200_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


