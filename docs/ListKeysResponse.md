# ListKeysResponse

Paginated list of HSM keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[HSMKeyMetadata]**](HSMKeyMetadata.md) | Array of HSM key metadata entries. | 
**count** | **int** | Total number of keys matching the query. | 

## Example

```python
from aqueduct_sdk.models.list_keys_response import ListKeysResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListKeysResponse from a JSON string
list_keys_response_instance = ListKeysResponse.from_json(json)
# print the JSON string representation of the object
print(ListKeysResponse.to_json())

# convert the object into a dict
list_keys_response_dict = list_keys_response_instance.to_dict()
# create an instance of ListKeysResponse from a dict
list_keys_response_from_dict = ListKeysResponse.from_dict(list_keys_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


