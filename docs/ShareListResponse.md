# ShareListResponse

List of shares for a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | [**List[ShareRecord]**](ShareRecord.md) |  | 

## Example

```python
from aqueduct_sdk.models.share_list_response import ShareListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShareListResponse from a JSON string
share_list_response_instance = ShareListResponse.from_json(json)
# print the JSON string representation of the object
print(ShareListResponse.to_json())

# convert the object into a dict
share_list_response_dict = share_list_response_instance.to_dict()
# create an instance of ShareListResponse from a dict
share_list_response_from_dict = ShareListResponse.from_dict(share_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


