# DLPDeidentifyResponseTransformationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_type** | **str** |  | [optional] 
**operator** | **str** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_deidentify_response_transformations_inner import DLPDeidentifyResponseTransformationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DLPDeidentifyResponseTransformationsInner from a JSON string
dlp_deidentify_response_transformations_inner_instance = DLPDeidentifyResponseTransformationsInner.from_json(json)
# print the JSON string representation of the object
print(DLPDeidentifyResponseTransformationsInner.to_json())

# convert the object into a dict
dlp_deidentify_response_transformations_inner_dict = dlp_deidentify_response_transformations_inner_instance.to_dict()
# create an instance of DLPDeidentifyResponseTransformationsInner from a dict
dlp_deidentify_response_transformations_inner_from_dict = DLPDeidentifyResponseTransformationsInner.from_dict(dlp_deidentify_response_transformations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


