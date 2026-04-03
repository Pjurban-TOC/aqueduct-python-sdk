# DLPPolicyRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_type** | [**InfoType**](InfoType.md) |  | 
**action** | **str** | Action to take when this info type is detected. | 
**min_score** | **float** | Minimum confidence score to trigger this rule. | [optional] [default to 0.7]
**deidentify_operator** | [**DeidentifyOperator**](DeidentifyOperator.md) |  | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_policy_rule import DLPPolicyRule

# TODO update the JSON string below
json = "{}"
# create an instance of DLPPolicyRule from a JSON string
dlp_policy_rule_instance = DLPPolicyRule.from_json(json)
# print the JSON string representation of the object
print(DLPPolicyRule.to_json())

# convert the object into a dict
dlp_policy_rule_dict = dlp_policy_rule_instance.to_dict()
# create an instance of DLPPolicyRule from a dict
dlp_policy_rule_from_dict = DLPPolicyRule.from_dict(dlp_policy_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


