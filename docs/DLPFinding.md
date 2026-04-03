# DLPFinding

Single PII detection finding. Multi-stage detection (pattern -> NER -> ML) per SafeGPT [arXiv:2601.06366] achieving 92% precision. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_type** | [**InfoType**](InfoType.md) |  | 
**likelihood** | **str** | Google DLP v2 likelihood scale. | 
**score** | **float** | Confidence score from the detection model. | 
**location** | [**DLPFindingLocation**](DLPFindingLocation.md) |  | 
**quote** | **str** | The matched text. Only included if the caller has sufficient permissions. | [optional] 
**detection_method** | **str** | Detection method that produced this finding. Multi-stage pipeline per SafeGPT architecture.  | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_finding import DLPFinding

# TODO update the JSON string below
json = "{}"
# create an instance of DLPFinding from a JSON string
dlp_finding_instance = DLPFinding.from_json(json)
# print the JSON string representation of the object
print(DLPFinding.to_json())

# convert the object into a dict
dlp_finding_dict = dlp_finding_instance.to_dict()
# create an instance of DLPFinding from a dict
dlp_finding_from_dict = DLPFinding.from_dict(dlp_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


