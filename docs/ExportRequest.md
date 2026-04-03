# ExportRequest

Export request. Matches handler/export.go ExportRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**user_id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**format** | **str** | Export format. | 

## Example

```python
from aqueduct_sdk.models.export_request import ExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRequest from a JSON string
export_request_instance = ExportRequest.from_json(json)
# print the JSON string representation of the object
print(ExportRequest.to_json())

# convert the object into a dict
export_request_dict = export_request_instance.to_dict()
# create an instance of ExportRequest from a dict
export_request_from_dict = ExportRequest.from_dict(export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


