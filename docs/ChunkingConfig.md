# ChunkingConfig

Document chunking strategy configuration. Per Merola & Singh [arXiv:2504.19754], contextual retrieval preserves coherence but costs more compute. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | **str** | Chunking strategy: - &#x60;fixed&#x60;: Split at character/token boundaries - &#x60;semantic&#x60;: Split at sentence/paragraph boundaries - &#x60;late&#x60;: Late chunking after embedding full document - &#x60;contextual&#x60;: Contextual retrieval with document-level context prepended  | [optional] [default to 'semantic']
**max_chunk_size** | **int** | Maximum chunk size in tokens. | [optional] [default to 512]
**chunk_overlap** | **int** | Overlap between adjacent chunks in tokens. | [optional] [default to 50]

## Example

```python
from aqueduct_sdk.models.chunking_config import ChunkingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkingConfig from a JSON string
chunking_config_instance = ChunkingConfig.from_json(json)
# print the JSON string representation of the object
print(ChunkingConfig.to_json())

# convert the object into a dict
chunking_config_dict = chunking_config_instance.to_dict()
# create an instance of ChunkingConfig from a dict
chunking_config_from_dict = ChunkingConfig.from_dict(chunking_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


