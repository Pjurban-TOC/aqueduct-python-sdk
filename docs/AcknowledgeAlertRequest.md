# AcknowledgeAlertRequest

Request to acknowledge a performance alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged_by** | **str** | User ID of the acknowledger. | 
**note** | **str** | Optional note about the acknowledgement. | [optional] 

## Example

```python
from aqueduct_sdk.models.acknowledge_alert_request import AcknowledgeAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeAlertRequest from a JSON string
acknowledge_alert_request_instance = AcknowledgeAlertRequest.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeAlertRequest.to_json())

# convert the object into a dict
acknowledge_alert_request_dict = acknowledge_alert_request_instance.to_dict()
# create an instance of AcknowledgeAlertRequest from a dict
acknowledge_alert_request_from_dict = AcknowledgeAlertRequest.from_dict(acknowledge_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


