# RetrievalRequest

Knowledge base retrieval request. Supports hybrid dense/sparse search per DAT [arXiv:2503.23013] which shows 26-31% NDCG improvement. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base_id** | **str** |  | 
**query** | **str** | Natural language query. | 
**top_k** | **int** | Number of results to return. | [optional] [default to 5]
**score_threshold** | **float** | Minimum relevance score to include a result. | [optional] [default to 0.3]
**filter** | **Dict[str, object]** | Metadata filter to narrow search scope. | [optional] 
**reranking** | [**RetrievalRequestReranking**](RetrievalRequestReranking.md) |  | [optional] 
**search_type** | **str** | Search strategy: - &#x60;similarity&#x60;: Pure dense vector similarity - &#x60;mmr&#x60;: Maximal Marginal Relevance (diversity-weighted) - &#x60;hybrid&#x60;: Combined dense + sparse (BM25) per DAT [arXiv:2503.23013]  | [optional] [default to 'hybrid']
**hybrid_weights** | [**RetrievalRequestHybridWeights**](RetrievalRequestHybridWeights.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.retrieval_request import RetrievalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalRequest from a JSON string
retrieval_request_instance = RetrievalRequest.from_json(json)
# print the JSON string representation of the object
print(RetrievalRequest.to_json())

# convert the object into a dict
retrieval_request_dict = retrieval_request_instance.to_dict()
# create an instance of RetrievalRequest from a dict
retrieval_request_from_dict = RetrievalRequest.from_dict(retrieval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


