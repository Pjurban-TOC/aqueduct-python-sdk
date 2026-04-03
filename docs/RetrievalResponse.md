# RetrievalResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[RetrievalResult]**](RetrievalResult.md) |  | 
**query_embedding_time_ms** | **int** | Time to embed the query in milliseconds. | [optional] 
**search_time_ms** | **int** | Vector search time in milliseconds. | [optional] 
**rerank_time_ms** | **int** | Reranking time in milliseconds (if enabled). | [optional] 

## Example

```python
from aqueduct_sdk.models.retrieval_response import RetrievalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalResponse from a JSON string
retrieval_response_instance = RetrievalResponse.from_json(json)
# print the JSON string representation of the object
print(RetrievalResponse.to_json())

# convert the object into a dict
retrieval_response_dict = retrieval_response_instance.to_dict()
# create an instance of RetrievalResponse from a dict
retrieval_response_from_dict = RetrievalResponse.from_dict(retrieval_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


