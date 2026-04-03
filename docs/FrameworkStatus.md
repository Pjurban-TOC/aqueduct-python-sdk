# FrameworkStatus

Compliance status summary for a single framework. Matches compliance-engine FrameworkStatus struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**framework_id** | **str** | Framework identifier. | 
**framework_name** | **str** | Human-readable framework name. | 
**compliance_percentage** | **float** | Percentage of controls meeting compliance (0-100). | 
**overall_status** | [**ControlStatus**](ControlStatus.md) |  | 

## Example

```python
from aqueduct_sdk.models.framework_status import FrameworkStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FrameworkStatus from a JSON string
framework_status_instance = FrameworkStatus.from_json(json)
# print the JSON string representation of the object
print(FrameworkStatus.to_json())

# convert the object into a dict
framework_status_dict = framework_status_instance.to_dict()
# create an instance of FrameworkStatus from a dict
framework_status_from_dict = FrameworkStatus.from_dict(framework_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


