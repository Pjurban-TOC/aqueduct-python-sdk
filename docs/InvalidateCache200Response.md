# InvalidateCache200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalidated_count** | **int** |  | [optional] 
**duration_ms** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.invalidate_cache200_response import InvalidateCache200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateCache200Response from a JSON string
invalidate_cache200_response_instance = InvalidateCache200Response.from_json(json)
# print the JSON string representation of the object
print(InvalidateCache200Response.to_json())

# convert the object into a dict
invalidate_cache200_response_dict = invalidate_cache200_response_instance.to_dict()
# create an instance of InvalidateCache200Response from a dict
invalidate_cache200_response_from_dict = InvalidateCache200Response.from_dict(invalidate_cache200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


