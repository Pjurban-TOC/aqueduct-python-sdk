# EmbeddingResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**embedding** | **List[float]** |  | 
**index** | **int** |  | 

## Example

```python
from aqueduct_sdk.models.embedding_response_data_inner import EmbeddingResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingResponseDataInner from a JSON string
embedding_response_data_inner_instance = EmbeddingResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(EmbeddingResponseDataInner.to_json())

# convert the object into a dict
embedding_response_data_inner_dict = embedding_response_data_inner_instance.to_dict()
# create an instance of EmbeddingResponseDataInner from a dict
embedding_response_data_inner_from_dict = EmbeddingResponseDataInner.from_dict(embedding_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


