# InvalidateResponseCache200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_count** | **int** | Number of cache entries removed. | 

## Example

```python
from aqueduct_sdk.models.invalidate_response_cache200_response import InvalidateResponseCache200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidateResponseCache200Response from a JSON string
invalidate_response_cache200_response_instance = InvalidateResponseCache200Response.from_json(json)
# print the JSON string representation of the object
print(InvalidateResponseCache200Response.to_json())

# convert the object into a dict
invalidate_response_cache200_response_dict = invalidate_response_cache200_response_instance.to_dict()
# create an instance of InvalidateResponseCache200Response from a dict
invalidate_response_cache200_response_from_dict = InvalidateResponseCache200Response.from_dict(invalidate_response_cache200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


