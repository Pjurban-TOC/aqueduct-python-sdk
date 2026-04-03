# FrameworkListResponse

Response containing the list of available compliance frameworks. Matches compliance-engine FrameworkListResponse struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frameworks** | [**List[ComplianceFramework]**](ComplianceFramework.md) | Available compliance frameworks. | 

## Example

```python
from aqueduct_sdk.models.framework_list_response import FrameworkListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FrameworkListResponse from a JSON string
framework_list_response_instance = FrameworkListResponse.from_json(json)
# print the JSON string representation of the object
print(FrameworkListResponse.to_json())

# convert the object into a dict
framework_list_response_dict = framework_list_response_instance.to_dict()
# create an instance of FrameworkListResponse from a dict
framework_list_response_from_dict = FrameworkListResponse.from_dict(framework_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


