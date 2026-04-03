# ExportSummary

Data export artifact details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Pre-signed download URL for the export archive. | 
**expires_at** | **datetime** | Timestamp when the export download URL expires. | 
**size_bytes** | **int** | Size of the export archive in bytes. | 

## Example

```python
from aqueduct_sdk.models.export_summary import ExportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ExportSummary from a JSON string
export_summary_instance = ExportSummary.from_json(json)
# print the JSON string representation of the object
print(ExportSummary.to_json())

# convert the object into a dict
export_summary_dict = export_summary_instance.to_dict()
# create an instance of ExportSummary from a dict
export_summary_from_dict = ExportSummary.from_dict(export_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


