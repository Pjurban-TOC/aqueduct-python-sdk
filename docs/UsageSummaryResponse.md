# UsageSummaryResponse

Tenant usage summary. Matches `tenants.go:88` UsageSummaryResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users_count** | **int** |  | [optional] 
**requests_this_month** | **int** |  | [optional] 
**storage_used_gb** | **float** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.usage_summary_response import UsageSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSummaryResponse from a JSON string
usage_summary_response_instance = UsageSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(UsageSummaryResponse.to_json())

# convert the object into a dict
usage_summary_response_dict = usage_summary_response_instance.to_dict()
# create an instance of UsageSummaryResponse from a dict
usage_summary_response_from_dict = UsageSummaryResponse.from_dict(usage_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


