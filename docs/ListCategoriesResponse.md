# ListCategoriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CUICategory]**](CUICategory.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_categories_response import ListCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCategoriesResponse from a JSON string
list_categories_response_instance = ListCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListCategoriesResponse.to_json())

# convert the object into a dict
list_categories_response_dict = list_categories_response_instance.to_dict()
# create an instance of ListCategoriesResponse from a dict
list_categories_response_from_dict = ListCategoriesResponse.from_dict(list_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


