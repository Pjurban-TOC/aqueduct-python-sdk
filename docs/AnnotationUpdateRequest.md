# AnnotationUpdateRequest

Request body for updating an annotation body.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Updated annotation text. | 

## Example

```python
from aqueduct_sdk.models.annotation_update_request import AnnotationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationUpdateRequest from a JSON string
annotation_update_request_instance = AnnotationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationUpdateRequest.to_json())

# convert the object into a dict
annotation_update_request_dict = annotation_update_request_instance.to_dict()
# create an instance of AnnotationUpdateRequest from a dict
annotation_update_request_from_dict = AnnotationUpdateRequest.from_dict(annotation_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


