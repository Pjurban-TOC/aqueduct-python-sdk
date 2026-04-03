# SafetyScanRequest

AI safety scan request. Multi-layer architecture per LlamaFirewall [Meta, arXiv:2505.03574]: input-guard -> reasoning-guard -> output-guard. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content to scan for safety violations. | 
**content_type** | **str** | Stage in the LLM pipeline this content belongs to. Per LlamaFirewall, each stage has a dedicated guard.  | [optional] [default to 'prompt']
**checks** | [**List[SafetyCheckType]**](SafetyCheckType.md) | Specific safety checks to run. If omitted, all configured checks are executed. Per Bypassing LLM Guardrails [arXiv:2504.11168], defense-in-depth with multiple checks is required.  | [optional] 
**guardrail_config_id** | **str** | Optional reference to a specific guardrail configuration. | [optional] 
**mode** | **str** | Guardrail execution mode. Per OneShield [arXiv:2507.21170]: - &#x60;sequential&#x60;: Run checks one by one (higher coverage, higher latency) - &#x60;unified&#x60;: Run all checks in a single pass (lower latency, may miss edge cases)  | [optional] [default to 'sequential']
**model** | **str** | Model context (some safety checks are model-specific). | [optional] 

## Example

```python
from aqueduct_sdk.models.safety_scan_request import SafetyScanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SafetyScanRequest from a JSON string
safety_scan_request_instance = SafetyScanRequest.from_json(json)
# print the JSON string representation of the object
print(SafetyScanRequest.to_json())

# convert the object into a dict
safety_scan_request_dict = safety_scan_request_instance.to_dict()
# create an instance of SafetyScanRequest from a dict
safety_scan_request_from_dict = SafetyScanRequest.from_dict(safety_scan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


