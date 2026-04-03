# SetAlertThreshold200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**threshold_id** | **str** |  | 

## Example

```python
from aqueduct_sdk.models.set_alert_threshold200_response import SetAlertThreshold200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SetAlertThreshold200Response from a JSON string
set_alert_threshold200_response_instance = SetAlertThreshold200Response.from_json(json)
# print the JSON string representation of the object
print(SetAlertThreshold200Response.to_json())

# convert the object into a dict
set_alert_threshold200_response_dict = set_alert_threshold200_response_instance.to_dict()
# create an instance of SetAlertThreshold200Response from a dict
set_alert_threshold200_response_from_dict = SetAlertThreshold200Response.from_dict(set_alert_threshold200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


