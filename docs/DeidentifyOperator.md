# DeidentifyOperator

De-identification operator configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Operator type. Per PrivacyRestore [arXiv:2406.01394], tokenize enables request-transform/response-restore architecture for reversible privacy.  | 
**replacement** | **str** | Replacement text (for &#x60;replace&#x60; type). | [optional] 
**masking_char** | **str** | Character used for masking (for &#x60;mask&#x60; type). | [optional] 
**chars_to_mask** | **int** | Number of characters to mask from the start (for &#x60;mask&#x60; type). | [optional] 
**hash_algorithm** | **str** | Hash algorithm (for &#x60;hash&#x60; type). | [optional] 
**crypto_key_name** | **str** | HSM key reference for encryption (for &#x60;encrypt&#x60; type). | [optional] 

## Example

```python
from aqueduct_sdk.models.deidentify_operator import DeidentifyOperator

# TODO update the JSON string below
json = "{}"
# create an instance of DeidentifyOperator from a JSON string
deidentify_operator_instance = DeidentifyOperator.from_json(json)
# print the JSON string representation of the object
print(DeidentifyOperator.to_json())

# convert the object into a dict
deidentify_operator_dict = deidentify_operator_instance.to_dict()
# create an instance of DeidentifyOperator from a dict
deidentify_operator_from_dict = DeidentifyOperator.from_dict(deidentify_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


