# SetThemePreferenceRequest

Request body for creating or updating a user's theme preference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**ThemeMode**](ThemeMode.md) |  | 
**reduced_motion** | **bool** | When true, disables animations per WCAG 2.2 SC 2.3.3 Motion Animation. | [optional] 
**system_high_contrast** | **bool** | When true, renders the UI in a high-contrast palette per WCAG 2.2 SC 1.4.11 Non-text Contrast. | [optional] 
**typography_scale** | **float** | Multiplier for base font size (1.0 &#x3D; default 16px). Supports WCAG 2.2 SC 1.4.4 Resize Text. | [optional] 

## Example

```python
from aqueduct_sdk.models.set_theme_preference_request import SetThemePreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetThemePreferenceRequest from a JSON string
set_theme_preference_request_instance = SetThemePreferenceRequest.from_json(json)
# print the JSON string representation of the object
print(SetThemePreferenceRequest.to_json())

# convert the object into a dict
set_theme_preference_request_dict = set_theme_preference_request_instance.to_dict()
# create an instance of SetThemePreferenceRequest from a dict
set_theme_preference_request_from_dict = SetThemePreferenceRequest.from_dict(set_theme_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


