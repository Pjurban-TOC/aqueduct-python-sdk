# DLPScanResponse

DLP scan results with detected PII findings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findings** | [**List[DLPFinding]**](DLPFinding.md) |  | 
**findings_count** | **int** |  | 
**scan_duration_ms** | **int** | Scan processing time in milliseconds. | 
**content_type** | **str** |  | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_scan_response import DLPScanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DLPScanResponse from a JSON string
dlp_scan_response_instance = DLPScanResponse.from_json(json)
# print the JSON string representation of the object
print(DLPScanResponse.to_json())

# convert the object into a dict
dlp_scan_response_dict = dlp_scan_response_instance.to_dict()
# create an instance of DLPScanResponse from a dict
dlp_scan_response_from_dict = DLPScanResponse.from_dict(dlp_scan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


