# ThemePreferenceResponse

Wrapper following SuccessResponse pattern. Contains the resolved theme preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ThemePreference**](ThemePreference.md) |  | 

## Example

```python
from aqueduct_sdk.models.theme_preference_response import ThemePreferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThemePreferenceResponse from a JSON string
theme_preference_response_instance = ThemePreferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ThemePreferenceResponse.to_json())

# convert the object into a dict
theme_preference_response_dict = theme_preference_response_instance.to_dict()
# create an instance of ThemePreferenceResponse from a dict
theme_preference_response_from_dict = ThemePreferenceResponse.from_dict(theme_preference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


