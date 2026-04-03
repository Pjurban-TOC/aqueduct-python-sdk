# GetAuditStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | [**GetAuditStats200ResponseTimeRange**](GetAuditStats200ResponseTimeRange.md) |  | 
**totals** | [**GetAuditStats200ResponseTotals**](GetAuditStats200ResponseTotals.md) |  | 
**groups** | [**List[GetAuditStats200ResponseGroupsInner]**](GetAuditStats200ResponseGroupsInner.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.get_audit_stats200_response import GetAuditStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuditStats200Response from a JSON string
get_audit_stats200_response_instance = GetAuditStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetAuditStats200Response.to_json())

# convert the object into a dict
get_audit_stats200_response_dict = get_audit_stats200_response_instance.to_dict()
# create an instance of GetAuditStats200Response from a dict
get_audit_stats200_response_from_dict = GetAuditStats200Response.from_dict(get_audit_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


