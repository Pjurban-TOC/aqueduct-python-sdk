# DLPFindingLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Start byte offset in the content. | 
**end** | **int** | End byte offset in the content. | 

## Example

```python
from aqueduct_sdk.models.dlp_finding_location import DLPFindingLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DLPFindingLocation from a JSON string
dlp_finding_location_instance = DLPFindingLocation.from_json(json)
# print the JSON string representation of the object
print(DLPFindingLocation.to_json())

# convert the object into a dict
dlp_finding_location_dict = dlp_finding_location_instance.to_dict()
# create an instance of DLPFindingLocation from a dict
dlp_finding_location_from_dict = DLPFindingLocation.from_dict(dlp_finding_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


