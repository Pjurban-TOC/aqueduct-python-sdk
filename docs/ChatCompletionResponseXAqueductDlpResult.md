# ChatCompletionResponseXAqueductDlpResult

DLP scan summary for the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scanned** | **bool** |  | [optional] 
**findings_count** | **int** |  | [optional] 
**action** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.chat_completion_response_x_aqueduct_dlp_result import ChatCompletionResponseXAqueductDlpResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionResponseXAqueductDlpResult from a JSON string
chat_completion_response_x_aqueduct_dlp_result_instance = ChatCompletionResponseXAqueductDlpResult.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionResponseXAqueductDlpResult.to_json())

# convert the object into a dict
chat_completion_response_x_aqueduct_dlp_result_dict = chat_completion_response_x_aqueduct_dlp_result_instance.to_dict()
# create an instance of ChatCompletionResponseXAqueductDlpResult from a dict
chat_completion_response_x_aqueduct_dlp_result_from_dict = ChatCompletionResponseXAqueductDlpResult.from_dict(chat_completion_response_x_aqueduct_dlp_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


