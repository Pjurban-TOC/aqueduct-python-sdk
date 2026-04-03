# AnnotationRequest

Request body for creating an annotation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Annotation text. May contain @mention tokens. | 
**parent_annotation_id** | **str** | Optional parent annotation ID for threaded replies. | [optional] 

## Example

```python
from aqueduct_sdk.models.annotation_request import AnnotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRequest from a JSON string
annotation_request_instance = AnnotationRequest.from_json(json)
# print the JSON string representation of the object
print(AnnotationRequest.to_json())

# convert the object into a dict
annotation_request_dict = annotation_request_instance.to_dict()
# create an instance of AnnotationRequest from a dict
annotation_request_from_dict = AnnotationRequest.from_dict(annotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


