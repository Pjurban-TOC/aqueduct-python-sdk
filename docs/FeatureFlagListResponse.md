# FeatureFlagListResponse

List of all feature flags. Matches `config.go` FeatureFlagListResponse struct.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | [**List[FeatureFlag]**](FeatureFlag.md) | Array of all feature flags. | 

## Example

```python
from aqueduct_sdk.models.feature_flag_list_response import FeatureFlagListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureFlagListResponse from a JSON string
feature_flag_list_response_instance = FeatureFlagListResponse.from_json(json)
# print the JSON string representation of the object
print(FeatureFlagListResponse.to_json())

# convert the object into a dict
feature_flag_list_response_dict = feature_flag_list_response_instance.to_dict()
# create an instance of FeatureFlagListResponse from a dict
feature_flag_list_response_from_dict = FeatureFlagListResponse.from_dict(feature_flag_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


