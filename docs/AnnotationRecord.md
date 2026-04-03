# AnnotationRecord

Comment anchored to a specific turn within a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Annotation identifier (UUID v4). | 
**tenant_id** | **str** |  | 
**conversation_id** | **str** |  | 
**turn_index** | **int** | Zero-based turn index within the conversation. | 
**author_user_id** | **str** |  | 
**body** | **str** | Annotation text. Supports @mention tokens (@username). | 
**parent_annotation_id** | **str** | Optional parent annotation ID for threaded replies. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.annotation_record import AnnotationRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationRecord from a JSON string
annotation_record_instance = AnnotationRecord.from_json(json)
# print the JSON string representation of the object
print(AnnotationRecord.to_json())

# convert the object into a dict
annotation_record_dict = annotation_record_instance.to_dict()
# create an instance of AnnotationRecord from a dict
annotation_record_from_dict = AnnotationRecord.from_dict(annotation_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


