# DLPScanRequest

Content scanning request for PII and sensitive data detection. Supports bidirectional scanning (prompts AND responses) per PII-Scope [arXiv:2410.06704] which shows existing evaluations underestimate leakage by 5x. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Text content to scan for sensitive data. | 
**content_type** | **str** | Context of the content being scanned. Bidirectional scanning (prompts AND responses) is mandatory per PII-Scope research.  | [optional] [default to 'prompt']
**info_types** | [**List[InfoType]**](InfoType.md) | Specific PII entity types to scan for. If omitted, all configured types are scanned. 18+ types from Microsoft Presidio.  | [optional] 
**score_threshold** | **float** | Minimum confidence score to report a finding. Per GLiNER [NAACL 2024], pluggable NER models produce calibrated confidence scores.  | [optional] [default to 0.5]
**language** | **str** | Language of the content for NER model selection. | [optional] [default to 'en']

## Example

```python
from aqueduct_sdk.models.dlp_scan_request import DLPScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DLPScanRequest from a JSON string
dlp_scan_request_instance = DLPScanRequest.from_json(json)
# print the JSON string representation of the object
print(DLPScanRequest.to_json())

# convert the object into a dict
dlp_scan_request_dict = dlp_scan_request_instance.to_dict()
# create an instance of DLPScanRequest from a dict
dlp_scan_request_from_dict = DLPScanRequest.from_dict(dlp_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


