# SafetyScanResponse

Safety scan result with per-check findings. Per Bypassing LLM Guardrails [arXiv:2504.11168] which achieves 100% evasion against individual guards, defense-in-depth with per-layer pass/fail reporting is required. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safe** | **bool** | Overall safety verdict. | 
**action** | **str** | Recommended action based on safety findings. | 
**findings** | [**List[SafetyFinding]**](SafetyFinding.md) |  | 
**modified_content** | **str** | Modified content with unsafe portions removed or transformed. Only present when action is &#x60;modify&#x60;. Per Defending Against Jailbreaks [arXiv:2511.18933], request transformation as pre-processing before model routing.  | [optional] 
**scan_duration_ms** | **int** | Total scan time in milliseconds. | [optional] 
**checks_performed** | [**List[SafetyCheckType]**](SafetyCheckType.md) |  | [optional] 
**guard_layer** | **str** | Which LlamaFirewall guard layer performed this scan. | [optional] 

## Example

```python
from aqueduct_sdk.models.safety_scan_response import SafetyScanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyScanResponse from a JSON string
safety_scan_response_instance = SafetyScanResponse.from_json(json)
# print the JSON string representation of the object
print(SafetyScanResponse.to_json())

# convert the object into a dict
safety_scan_response_dict = safety_scan_response_instance.to_dict()
# create an instance of SafetyScanResponse from a dict
safety_scan_response_from_dict = SafetyScanResponse.from_dict(safety_scan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


