# DLPDeidentifyRequest

Content de-identification request with per-info-type operator configuration. Per PAPILLON [IJCAI 2025], PII redaction modes (mask/tokenize/remove) should be configurable policy options. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Text content to de-identify. | 
**deidentify_config** | [**DLPDeidentifyRequestDeidentifyConfig**](DLPDeidentifyRequestDeidentifyConfig.md) |  | 
**content_type** | **str** |  | [optional] [default to 'prompt']

## Example

```python
from aqueduct_sdk.models.dlp_deidentify_request import DLPDeidentifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DLPDeidentifyRequest from a JSON string
dlp_deidentify_request_instance = DLPDeidentifyRequest.from_json(json)
# print the JSON string representation of the object
print(DLPDeidentifyRequest.to_json())

# convert the object into a dict
dlp_deidentify_request_dict = dlp_deidentify_request_instance.to_dict()
# create an instance of DLPDeidentifyRequest from a dict
dlp_deidentify_request_from_dict = DLPDeidentifyRequest.from_dict(dlp_deidentify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


