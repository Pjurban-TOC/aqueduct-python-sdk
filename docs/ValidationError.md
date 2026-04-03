# ValidationError

Single field validation error. Matches `common/errors/rfc7807.go:51` ValidationError struct. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field path using dot notation (e.g., &#x60;messages[0].content&#x60;). | 
**message** | **str** | Human-readable error message for this field. | 
**code** | **str** | Machine-readable validation code (required, min_length, pattern, etc.). | 

## Example

```python
from aqueduct_sdk.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


