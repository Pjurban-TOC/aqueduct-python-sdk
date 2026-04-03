# AnnotationListResponse

List of annotations for a conversation turn.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**List[AnnotationRecord]**](AnnotationRecord.md) |  | 

## Example

```python
from aqueduct_sdk.models.annotation_list_response import AnnotationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationListResponse from a JSON string
annotation_list_response_instance = AnnotationListResponse.from_json(json)
# print the JSON string representation of the object
print(AnnotationListResponse.to_json())

# convert the object into a dict
annotation_list_response_dict = annotation_list_response_instance.to_dict()
# create an instance of AnnotationListResponse from a dict
annotation_list_response_from_dict = AnnotationListResponse.from_dict(annotation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


