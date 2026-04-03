# UpdateKnowledgeBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**chunking_config** | [**ChunkingConfig**](ChunkingConfig.md) |  | [optional] 
**privacy_config** | [**RAGPrivacyConfig**](RAGPrivacyConfig.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.update_knowledge_base_request import UpdateKnowledgeBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKnowledgeBaseRequest from a JSON string
update_knowledge_base_request_instance = UpdateKnowledgeBaseRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateKnowledgeBaseRequest.to_json())

# convert the object into a dict
update_knowledge_base_request_dict = update_knowledge_base_request_instance.to_dict()
# create an instance of UpdateKnowledgeBaseRequest from a dict
update_knowledge_base_request_from_dict = UpdateKnowledgeBaseRequest.from_dict(update_knowledge_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


