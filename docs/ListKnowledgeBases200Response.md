# ListKnowledgeBases200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_bases** | [**List[KnowledgeBase]**](KnowledgeBase.md) |  | [optional] 
**next_cursor** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_knowledge_bases200_response import ListKnowledgeBases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKnowledgeBases200Response from a JSON string
list_knowledge_bases200_response_instance = ListKnowledgeBases200Response.from_json(json)
# print the JSON string representation of the object
print(ListKnowledgeBases200Response.to_json())

# convert the object into a dict
list_knowledge_bases200_response_dict = list_knowledge_bases200_response_instance.to_dict()
# create an instance of ListKnowledgeBases200Response from a dict
list_knowledge_bases200_response_from_dict = ListKnowledgeBases200Response.from_dict(list_knowledge_bases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


