# DeleteSession200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminated** | **bool** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.delete_session200_response import DeleteSession200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSession200Response from a JSON string
delete_session200_response_instance = DeleteSession200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteSession200Response.to_json())

# convert the object into a dict
delete_session200_response_dict = delete_session200_response_instance.to_dict()
# create an instance of DeleteSession200Response from a dict
delete_session200_response_from_dict = DeleteSession200Response.from_dict(delete_session200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


