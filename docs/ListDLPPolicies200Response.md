# ListDLPPolicies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[DLPPolicy]**](DLPPolicy.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_dlp_policies200_response import ListDLPPolicies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDLPPolicies200Response from a JSON string
list_dlp_policies200_response_instance = ListDLPPolicies200Response.from_json(json)
# print the JSON string representation of the object
print(ListDLPPolicies200Response.to_json())

# convert the object into a dict
list_dlp_policies200_response_dict = list_dlp_policies200_response_instance.to_dict()
# create an instance of ListDLPPolicies200Response from a dict
list_dlp_policies200_response_from_dict = ListDLPPolicies200Response.from_dict(list_dlp_policies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


