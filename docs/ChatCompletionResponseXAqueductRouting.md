# ChatCompletionResponseXAqueductRouting

Model routing metadata. Per TensorOpera Router [arXiv:2408.12320] and UniRoute [arXiv:2502.08773]. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** |  | [optional] 
**candidates_evaluated** | **int** |  | [optional] 
**selection_reason** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_response_x_aqueduct_routing import ChatCompletionResponseXAqueductRouting

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionResponseXAqueductRouting from a JSON string
chat_completion_response_x_aqueduct_routing_instance = ChatCompletionResponseXAqueductRouting.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionResponseXAqueductRouting.to_json())

# convert the object into a dict
chat_completion_response_x_aqueduct_routing_dict = chat_completion_response_x_aqueduct_routing_instance.to_dict()
# create an instance of ChatCompletionResponseXAqueductRouting from a dict
chat_completion_response_x_aqueduct_routing_from_dict = ChatCompletionResponseXAqueductRouting.from_dict(chat_completion_response_x_aqueduct_routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


