# TemporaryIncreaseReq

Temporary quota increase parameters. Matches `quotas.go:111` TemporaryIncreaseReq.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Resource to temporarily increase. | 
**amount** | **int** | Additional units to grant temporarily. | 
**expires_at** | **datetime** | When the temporary increase expires. Must be in the future. | 

## Example

```python
from aqueduct_sdk.models.temporary_increase_req import TemporaryIncreaseReq

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryIncreaseReq from a JSON string
temporary_increase_req_instance = TemporaryIncreaseReq.from_json(json)
# print the JSON string representation of the object
print(TemporaryIncreaseReq.to_json())

# convert the object into a dict
temporary_increase_req_dict = temporary_increase_req_instance.to_dict()
# create an instance of TemporaryIncreaseReq from a dict
temporary_increase_req_from_dict = TemporaryIncreaseReq.from_dict(temporary_increase_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


