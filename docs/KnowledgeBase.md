# KnowledgeBase

Knowledge base resource for RAG retrieval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kb_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**embedding_model** | **str** | Model used for document embeddings. | [optional] 
**chunking_config** | [**ChunkingConfig**](ChunkingConfig.md) |  | [optional] 
**vector_store_config** | [**KnowledgeBaseVectorStoreConfig**](KnowledgeBaseVectorStoreConfig.md) |  | [optional] 
**document_count** | **int** |  | [optional] 
**total_chunks** | **int** |  | [optional] 
**status** | **str** |  | 
**privacy_config** | [**RAGPrivacyConfig**](RAGPrivacyConfig.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.knowledge_base import KnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBase from a JSON string
knowledge_base_instance = KnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBase.to_json())

# convert the object into a dict
knowledge_base_dict = knowledge_base_instance.to_dict()
# create an instance of KnowledgeBase from a dict
knowledge_base_from_dict = KnowledgeBase.from_dict(knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


