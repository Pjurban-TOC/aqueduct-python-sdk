# ControlListResponse

Response containing the list of controls for a framework. Matches compliance-engine ControlListResponse struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controls** | [**List[ComplianceControl]**](ComplianceControl.md) | Controls belonging to the requested framework. | 

## Example

```python
from aqueduct_sdk.models.control_list_response import ControlListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlListResponse from a JSON string
control_list_response_instance = ControlListResponse.from_json(json)
# print the JSON string representation of the object
print(ControlListResponse.to_json())

# convert the object into a dict
control_list_response_dict = control_list_response_instance.to_dict()
# create an instance of ControlListResponse from a dict
control_list_response_from_dict = ControlListResponse.from_dict(control_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


