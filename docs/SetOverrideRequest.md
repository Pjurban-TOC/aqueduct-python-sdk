# SetOverrideRequest

Request body for setting a tenant-level configuration override. Matches `config.go` SetOverrideRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | Override value for this configuration key within the tenant scope. | 
**type** | **str** | Optionally change the data type for this tenant override. | [optional] 
**description** | **str** | Reason or description for this tenant-specific override. | [optional] 

## Example

```python
from aqueduct_sdk.models.set_override_request import SetOverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOverrideRequest from a JSON string
set_override_request_instance = SetOverrideRequest.from_json(json)
# print the JSON string representation of the object
print(SetOverrideRequest.to_json())

# convert the object into a dict
set_override_request_dict = set_override_request_instance.to_dict()
# create an instance of SetOverrideRequest from a dict
set_override_request_from_dict = SetOverrideRequest.from_dict(set_override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


