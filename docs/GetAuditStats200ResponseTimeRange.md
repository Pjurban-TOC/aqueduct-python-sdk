# GetAuditStats200ResponseTimeRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_audit_stats200_response_time_range import GetAuditStats200ResponseTimeRange

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditStats200ResponseTimeRange from a JSON string
get_audit_stats200_response_time_range_instance = GetAuditStats200ResponseTimeRange.from_json(json)
# print the JSON string representation of the object
print(GetAuditStats200ResponseTimeRange.to_json())

# convert the object into a dict
get_audit_stats200_response_time_range_dict = get_audit_stats200_response_time_range_instance.to_dict()
# create an instance of GetAuditStats200ResponseTimeRange from a dict
get_audit_stats200_response_time_range_from_dict = GetAuditStats200ResponseTimeRange.from_dict(get_audit_stats200_response_time_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


