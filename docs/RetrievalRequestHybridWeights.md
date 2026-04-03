# RetrievalRequestHybridWeights

Weights for hybrid search (when search_type=hybrid).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dense** | **float** |  | [optional] [default to 0.7]
**sparse** | **float** |  | [optional] [default to 0.3]

## Example

```python
from aqueduct_sdk.models.retrieval_request_hybrid_weights import RetrievalRequestHybridWeights

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalRequestHybridWeights from a JSON string
retrieval_request_hybrid_weights_instance = RetrievalRequestHybridWeights.from_json(json)
# print the JSON string representation of the object
print(RetrievalRequestHybridWeights.to_json())

# convert the object into a dict
retrieval_request_hybrid_weights_dict = retrieval_request_hybrid_weights_instance.to_dict()
# create an instance of RetrievalRequestHybridWeights from a dict
retrieval_request_hybrid_weights_from_dict = RetrievalRequestHybridWeights.from_dict(retrieval_request_hybrid_weights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


