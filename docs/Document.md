# Document

Document in a knowledge base.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | 
**name** | **str** |  | 
**content_type** | **str** | MIME type of the source document. | [optional] 
**source** | [**DocumentSource**](DocumentSource.md) |  | [optional] 
**metadata** | **Dict[str, object]** | User-defined metadata for filtering during retrieval. | [optional] 
**chunk_count** | **int** |  | [optional] 
**status** | **str** |  | 
**error_message** | **str** | Error details if status is &#x60;error&#x60;. | [optional] 
**created_at** | **datetime** |  | 
**indexed_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


