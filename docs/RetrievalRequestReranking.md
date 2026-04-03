# RetrievalRequestReranking

Configurable re-ranking per TREC 2025 RAG Track [arXiv:2603.09891]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]
**model** | **str** | Reranking model to use. | [optional] 
**top_n** | **int** | Number of results to return after reranking. | [optional] 

## Example

```python
from aqueduct_sdk.models.retrieval_request_reranking import RetrievalRequestReranking

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalRequestReranking from a JSON string
retrieval_request_reranking_instance = RetrievalRequestReranking.from_json(json)
# print the JSON string representation of the object
print(RetrievalRequestReranking.to_json())

# convert the object into a dict
retrieval_request_reranking_dict = retrieval_request_reranking_instance.to_dict()
# create an instance of RetrievalRequestReranking from a dict
retrieval_request_reranking_from_dict = RetrievalRequestReranking.from_dict(retrieval_request_reranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


