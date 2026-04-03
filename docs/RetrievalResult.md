# RetrievalResult

Single retrieval result with trust/confidence scores per Engineering the RAG Stack [arXiv:2601.05264]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Retrieved chunk text. | 
**score** | **float** | Relevance score. | 
**source** | [**RetrievalResultSource**](RetrievalResultSource.md) |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**trust_score** | **float** | Trust/confidence score indicating retrieval quality. Per Engineering the RAG Stack [arXiv:2601.05264].  | [optional] 

## Example

```python
from aqueduct_sdk.models.retrieval_result import RetrievalResult

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalResult from a JSON string
retrieval_result_instance = RetrievalResult.from_json(json)
# print the JSON string representation of the object
print(RetrievalResult.to_json())

# convert the object into a dict
retrieval_result_dict = retrieval_result_instance.to_dict()
# create an instance of RetrievalResult from a dict
retrieval_result_from_dict = RetrievalResult.from_dict(retrieval_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


