# ApplyMarkingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | Unique identifier of the data object to mark. | 
**resource_type** | **str** | Type of data object (e.g., \&quot;document\&quot;, \&quot;record\&quot;). | 
**categories** | **List[str]** | CUI category codes from the NARA registry. | 
**dissemination_controls** | **List[str]** | Limited Dissemination Control codes. | [optional] 
**releasable_to** | **List[str]** | ISO 3166-1 alpha-3 country codes for REL TO. | [optional] 
**controlled_by** | **str** | Originating organization. | [optional] 
**decontrol_date** | **date** | ISO 8601 decontrol date. | [optional] 
**decontrol_event** | **str** | Event that triggers decontrol. | [optional] 

## Example

```python
from aqueduct_sdk.models.apply_marking_request import ApplyMarkingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyMarkingRequest from a JSON string
apply_marking_request_instance = ApplyMarkingRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyMarkingRequest.to_json())

# convert the object into a dict
apply_marking_request_dict = apply_marking_request_instance.to_dict()
# create an instance of ApplyMarkingRequest from a dict
apply_marking_request_from_dict = ApplyMarkingRequest.from_dict(apply_marking_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


