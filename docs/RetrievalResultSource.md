# RetrievalResultSource

Source document metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**document_name** | **str** |  | [optional] 
**chunk_index** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.retrieval_result_source import RetrievalResultSource

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalResultSource from a JSON string
retrieval_result_source_instance = RetrievalResultSource.from_json(json)
# print the JSON string representation of the object
print(RetrievalResultSource.to_json())

# convert the object into a dict
retrieval_result_source_dict = retrieval_result_source_instance.to_dict()
# create an instance of RetrievalResultSource from a dict
retrieval_result_source_from_dict = RetrievalResultSource.from_dict(retrieval_result_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


