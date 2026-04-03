# DLPDeidentifyRequestDeidentifyConfig

Per-info-type de-identification operators.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_operator** | [**DeidentifyOperator**](DeidentifyOperator.md) |  | [optional] 
**info_type_operators** | [**Dict[str, DeidentifyOperator]**](DeidentifyOperator.md) | Operator overrides keyed by info type. | [optional] 

## Example

```python
from aqueduct_sdk.models.dlp_deidentify_request_deidentify_config import DLPDeidentifyRequestDeidentifyConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DLPDeidentifyRequestDeidentifyConfig from a JSON string
dlp_deidentify_request_deidentify_config_instance = DLPDeidentifyRequestDeidentifyConfig.from_json(json)
# print the JSON string representation of the object
print(DLPDeidentifyRequestDeidentifyConfig.to_json())

# convert the object into a dict
dlp_deidentify_request_deidentify_config_dict = dlp_deidentify_request_deidentify_config_instance.to_dict()
# create an instance of DLPDeidentifyRequestDeidentifyConfig from a dict
dlp_deidentify_request_deidentify_config_from_dict = DLPDeidentifyRequestDeidentifyConfig.from_dict(dlp_deidentify_request_deidentify_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


