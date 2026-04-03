# ListMarkingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markings** | [**List[StoredMarking]**](StoredMarking.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.list_markings_response import ListMarkingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMarkingsResponse from a JSON string
list_markings_response_instance = ListMarkingsResponse.from_json(json)
# print the JSON string representation of the object
print(ListMarkingsResponse.to_json())

# convert the object into a dict
list_markings_response_dict = list_markings_response_instance.to_dict()
# create an instance of ListMarkingsResponse from a dict
list_markings_response_from_dict = ListMarkingsResponse.from_dict(list_markings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


