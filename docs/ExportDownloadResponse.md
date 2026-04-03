# ExportDownloadResponse

Detailed export download status and artifact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_id** | **str** | Unique identifier for the export job. | 
**status** | **str** | Current export generation status. | 
**url** | **str** | Pre-signed download URL, or null if the export is not yet ready or has expired. | [optional] 
**expires_at** | **datetime** | Timestamp when the download URL expires, or null if not applicable. | [optional] 
**size_bytes** | **int** | Size of the export archive in bytes, or null if not yet computed. | [optional] 
**checksum** | **str** | SHA-256 checksum of the export archive for integrity verification, or null if not yet computed. | [optional] 

## Example

```python
from aqueduct_sdk.models.export_download_response import ExportDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportDownloadResponse from a JSON string
export_download_response_instance = ExportDownloadResponse.from_json(json)
# print the JSON string representation of the object
print(ExportDownloadResponse.to_json())

# convert the object into a dict
export_download_response_dict = export_download_response_instance.to_dict()
# create an instance of ExportDownloadResponse from a dict
export_download_response_from_dict = ExportDownloadResponse.from_dict(export_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


