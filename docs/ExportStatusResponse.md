# ExportStatusResponse

Export job status. Matches handler/export.go ExportStatusResponse.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **str** |  | 
**status** | **str** | Export job status. | 
**message** | **str** |  | [optional] 
**progress** | **int** | Progress percentage (0-100). | 
**download_url** | **str** | URL to download the export file (when completed). | [optional] 
**created_at** | **datetime** |  | 
**completed_at** | **datetime** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.export_status_response import ExportStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportStatusResponse from a JSON string
export_status_response_instance = ExportStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ExportStatusResponse.to_json())

# convert the object into a dict
export_status_response_dict = export_status_response_instance.to_dict()
# create an instance of ExportStatusResponse from a dict
export_status_response_from_dict = ExportStatusResponse.from_dict(export_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


