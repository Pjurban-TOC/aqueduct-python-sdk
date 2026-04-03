# CUICategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Category code (e.g., \&quot;SP-HLTH\&quot;, \&quot;PROPIN\&quot;). | 
**name** | **str** | Human-readable category name. | 
**specified** | **bool** | Whether this is a CUI Specified category (vs. Basic). | 
**index_group** | **str** | NARA index grouping. | 

## Example

```python
from aqueduct_sdk.models.cui_category import CUICategory

# TODO update the JSON string below
json = "{}"
# create an instance of CUICategory from a JSON string
cui_category_instance = CUICategory.from_json(json)
# print the JSON string representation of the object
print(CUICategory.to_json())

# convert the object into a dict
cui_category_dict = cui_category_instance.to_dict()
# create an instance of CUICategory from a dict
cui_category_from_dict = CUICategory.from_dict(cui_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


