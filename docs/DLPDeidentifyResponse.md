# DLPDeidentifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deidentified_content** | **str** | Content with PII replaced according to the de-identification config. | 
**transformations_count** | **int** |  | 
**transformations** | [**List[DLPDeidentifyResponseTransformationsInner]**](DLPDeidentifyResponseTransformationsInner.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_deidentify_response import DLPDeidentifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DLPDeidentifyResponse from a JSON string
dlp_deidentify_response_instance = DLPDeidentifyResponse.from_json(json)
# print the JSON string representation of the object
print(DLPDeidentifyResponse.to_json())

# convert the object into a dict
dlp_deidentify_response_dict = dlp_deidentify_response_instance.to_dict()
# create an instance of DLPDeidentifyResponse from a dict
dlp_deidentify_response_from_dict = DLPDeidentifyResponse.from_dict(dlp_deidentify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


