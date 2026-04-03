# CreateDLPPolicyRequest

Request body for creating a new DLP enforcement policy. The server assigns the policy_id on creation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | 
**scope** | **str** | Whether to scan requests, responses, or both. | [optional] [default to 'both']
**rules** | [**List[DLPPolicyRule]**](DLPPolicyRule.md) |  | 
**applies_to_models** | **List[str]** | Models this policy applies to. Empty &#x3D; all models. | [optional] 

## Example

```python
from aqueduct_sdk.models.create_dlp_policy_request import CreateDLPPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDLPPolicyRequest from a JSON string
create_dlp_policy_request_instance = CreateDLPPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDLPPolicyRequest.to_json())

# convert the object into a dict
create_dlp_policy_request_dict = create_dlp_policy_request_instance.to_dict()
# create an instance of CreateDLPPolicyRequest from a dict
create_dlp_policy_request_from_dict = CreateDLPPolicyRequest.from_dict(create_dlp_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


