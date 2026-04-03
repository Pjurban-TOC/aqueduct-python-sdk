# KnowledgeBaseVectorStoreConfig

Vector store backend configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**collection_name** | **str** |  | [optional] 
**dimensions** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.knowledge_base_vector_store_config import KnowledgeBaseVectorStoreConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseVectorStoreConfig from a JSON string
knowledge_base_vector_store_config_instance = KnowledgeBaseVectorStoreConfig.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseVectorStoreConfig.to_json())

# convert the object into a dict
knowledge_base_vector_store_config_dict = knowledge_base_vector_store_config_instance.to_dict()
# create an instance of KnowledgeBaseVectorStoreConfig from a dict
knowledge_base_vector_store_config_from_dict = KnowledgeBaseVectorStoreConfig.from_dict(knowledge_base_vector_store_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


