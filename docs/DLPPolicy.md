# DLPPolicy

DLP enforcement policy (response model). Policies support bidirectional scope (request/response/both) and model-specific application. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**scope** | **str** | Whether to scan requests, responses, or both. | [optional] [default to 'both']
**rules** | [**List[DLPPolicyRule]**](DLPPolicyRule.md) |  | 
**applies_to_models** | **List[str]** | Models this policy applies to. Empty &#x3D; all models. | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from aqueduct_sdk.models.dlp_policy import DLPPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DLPPolicy from a JSON string
dlp_policy_instance = DLPPolicy.from_json(json)
# print the JSON string representation of the object
print(DLPPolicy.to_json())

# convert the object into a dict
dlp_policy_dict = dlp_policy_instance.to_dict()
# create an instance of DLPPolicy from a dict
dlp_policy_from_dict = DLPPolicy.from_dict(dlp_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


