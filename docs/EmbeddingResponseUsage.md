# EmbeddingResponseUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | [optional] 
**total_tokens** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.embedding_response_usage import EmbeddingResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingResponseUsage from a JSON string
embedding_response_usage_instance = EmbeddingResponseUsage.from_json(json)
# print the JSON string representation of the object
print(EmbeddingResponseUsage.to_json())

# convert the object into a dict
embedding_response_usage_dict = embedding_response_usage_instance.to_dict()
# create an instance of EmbeddingResponseUsage from a dict
embedding_response_usage_from_dict = EmbeddingResponseUsage.from_dict(embedding_response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


