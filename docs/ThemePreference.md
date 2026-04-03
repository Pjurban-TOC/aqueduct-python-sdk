# ThemePreference

Persisted theme preference for a user within a tenant. Matches `preferences.go` ThemePreference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User identifier who owns this preference. | 
**tenant_id** | **str** | Tenant scope for the preference. | 
**mode** | [**ThemeMode**](ThemeMode.md) |  | 
**reduced_motion** | **bool** | When true, disables animations per WCAG 2.2 SC 2.3.3 Motion Animation. | [optional] 
**system_high_contrast** | **bool** | When true, renders the UI in a high-contrast palette per WCAG 2.2 SC 1.4.11 Non-text Contrast. | [optional] 
**typography_scale** | **float** | Multiplier for base font size (1.0 &#x3D; default 16px). Supports WCAG 2.2 SC 1.4.4 Resize Text. | [optional] 
**created_at** | **datetime** | Timestamp when the preference was first created. | [optional] 
**updated_at** | **datetime** | Timestamp when the preference was last modified. | [optional] 

## Example

```python
from aqueduct_sdk.models.theme_preference import ThemePreference

# TODO update the JSON string below
json = "{}"
# create an instance of ThemePreference from a JSON string
theme_preference_instance = ThemePreference.from_json(json)
# print the JSON string representation of the object
print(ThemePreference.to_json())

# convert the object into a dict
theme_preference_dict = theme_preference_instance.to_dict()
# create an instance of ThemePreference from a dict
theme_preference_from_dict = ThemePreference.from_dict(theme_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


