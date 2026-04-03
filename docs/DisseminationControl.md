# DisseminationControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Dissemination control code. | 
**name** | **str** | Human-readable name. | 
**description** | **str** |  | [optional] 
**legacy** | **bool** | Whether this is a retired control (e.g., FOUO). | 

## Example

```python
from aqueduct_sdk.models.dissemination_control import DisseminationControl

# TODO update the JSON string below
json = "{}"
# create an instance of DisseminationControl from a JSON string
dissemination_control_instance = DisseminationControl.from_json(json)
# print the JSON string representation of the object
print(DisseminationControl.to_json())

# convert the object into a dict
dissemination_control_dict = dissemination_control_instance.to_dict()
# create an instance of DisseminationControl from a dict
dissemination_control_from_dict = DisseminationControl.from_dict(dissemination_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


