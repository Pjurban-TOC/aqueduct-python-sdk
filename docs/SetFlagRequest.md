# SetFlagRequest

Request body for setting a feature flag value. Matches `config.go` SetFlagRequest struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether to enable or disable this feature flag. | 
**description** | **str** | Updated description for this feature flag. | [optional] 

## Example

```python
from aqueduct_sdk.models.set_flag_request import SetFlagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetFlagRequest from a JSON string
set_flag_request_instance = SetFlagRequest.from_json(json)
# print the JSON string representation of the object
print(SetFlagRequest.to_json())

# convert the object into a dict
set_flag_request_dict = set_flag_request_instance.to_dict()
# create an instance of SetFlagRequest from a dict
set_flag_request_from_dict = SetFlagRequest.from_dict(set_flag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


