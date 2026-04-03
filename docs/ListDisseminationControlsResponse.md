# ListDisseminationControlsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dissemination_controls** | [**List[DisseminationControl]**](DisseminationControl.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_dissemination_controls_response import ListDisseminationControlsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDisseminationControlsResponse from a JSON string
list_dissemination_controls_response_instance = ListDisseminationControlsResponse.from_json(json)
# print the JSON string representation of the object
print(ListDisseminationControlsResponse.to_json())

# convert the object into a dict
list_dissemination_controls_response_dict = list_dissemination_controls_response_instance.to_dict()
# create an instance of ListDisseminationControlsResponse from a dict
list_dissemination_controls_response_from_dict = ListDisseminationControlsResponse.from_dict(list_dissemination_controls_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


