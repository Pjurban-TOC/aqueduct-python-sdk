# EmbeddingRequestInput

Text(s) to embed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from aqueduct_sdk.models.embedding_request_input import EmbeddingRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingRequestInput from a JSON string
embedding_request_input_instance = EmbeddingRequestInput.from_json(json)
# print the JSON string representation of the object
print(EmbeddingRequestInput.to_json())

# convert the object into a dict
embedding_request_input_dict = embedding_request_input_instance.to_dict()
# create an instance of EmbeddingRequestInput from a dict
embedding_request_input_from_dict = EmbeddingRequestInput.from_dict(embedding_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


