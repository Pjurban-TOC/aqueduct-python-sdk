# AcknowledgeQuotaAlert200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | **bool** |  | [optional] 
**alert_id** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.acknowledge_quota_alert200_response import AcknowledgeQuotaAlert200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AcknowledgeQuotaAlert200Response from a JSON string
acknowledge_quota_alert200_response_instance = AcknowledgeQuotaAlert200Response.from_json(json)
# print the JSON string representation of the object
print(AcknowledgeQuotaAlert200Response.to_json())

# convert the object into a dict
acknowledge_quota_alert200_response_dict = acknowledge_quota_alert200_response_instance.to_dict()
# create an instance of AcknowledgeQuotaAlert200Response from a dict
acknowledge_quota_alert200_response_from_dict = AcknowledgeQuotaAlert200Response.from_dict(acknowledge_quota_alert200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


